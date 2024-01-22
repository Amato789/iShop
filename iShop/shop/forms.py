from django import forms
from .models import Review, Rating, RatingStar


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('text', )
        widget = {
            "text": forms.Textarea(attrs={"class": "form-control border"}),
        }


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None)

    class Meta:
        model = Rating
        fields = ("star",)
