from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from shop.models import Product


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='discounts')
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                   help_text='Percentage value (0 to 100)')
    active = models.BooleanField()

    def __str__(self):
        return str(self.discount)
