from decimal import Decimal
from django.conf import settings
from core.shop.models import Product
from core.discount.models import Discount


class Cart:
    def __init__(self, request):
        """Инициализиция корзины"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохранить пустую корзину в сеансе
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Прокрутить товарные позиции корзины в цикле и получить товары из БД
        """
        product_ids = self.cart.keys()
        # получить объекты product и добавить их в корзину
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            item['total_discount'] = Decimal(int(item['discount']) * item['quantity'])
            item['total_price_with_discount'] = Decimal(item['total_price'] - item['total_discount'])
            yield item

    def __len__(self):
        """Подсчитать все товарные позиции в корзине"""
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):
        """Добавить товар в корзину или обновить его"""
        product_id = str(product.id)
        try:
            discount = Discount.objects.get(product=product, active=True)
        except Discount.DoesNotExist:
            discount = 0
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price), 'discount': str(discount)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Пометить сеанс как измененный? чтобы потом обеспечить его сохранение
        self.session.modified = True

    def remove(self, product):
        """Удалить товар из корзины"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # удалить корзину из сеанса
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price_with_discount(self):
        return self.get_total_price() - self.get_total_discount()

    def get_total_discount(self):
        return sum(Decimal(item['price']) * item['quantity'] * Decimal(item['discount']) / 100 for item in self.cart.values())
