from django import forms
from .models import Wishlist


class WishlistAddForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields =['user', 'product']
