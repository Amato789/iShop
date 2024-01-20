from django import forms

PRODUCT_QUANTITY_CHOICES = 1


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
