from django import forms
from .models import Review, Rating


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('text', )
        widget = {
            "text": forms.Textarea(attrs={"class": "form-control border"}),
        }
