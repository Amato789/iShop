from django.db import models
from django.conf import settings
from shop.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist')
    created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ['user']
        indexes = [models.Index(fields=['user']), ]

    def __str__(self):
        return f'{self.user} - wishlist #{self.id}'
