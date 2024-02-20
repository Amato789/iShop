from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='categories', blank=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']), ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='brands', blank=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']), ]

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    def get_review(self):
        return self.reviews.filter(parent__isnull=True)

    def get_rating(self):
        return self.ratings.aggregate(models.Avg('star', default=0))['star__avg']

    def get_price_with_discount(self):
        try:
            discount = self.discounts.get(active=True)
        except:
            discount = None
        if discount is None:
            return ''
        return self.price * (100 - discount.discount) / 100
        # return self.discounts.get(active=True)


class ProductImages(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(max_length=1000)
    parent = models.ForeignKey('self',
                               verbose_name='Parent',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               related_name='children')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.product}'

    class Meta:
        indexes = [
            models.Index(fields=['product']),
        ]


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    star = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='ratings')

    def __str__(self):
        return str({self.pk})

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
