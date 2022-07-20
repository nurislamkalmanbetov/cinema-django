from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Review Forms"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
