from django import forms
from .models import feeds_list


class feedform(forms.ModelForm):
    class Meta:
        model = feeds_list
        fields = ("feed",)
