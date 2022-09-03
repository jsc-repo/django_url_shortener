from django import forms
from .models import Question


class UrlForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("original_url",)
