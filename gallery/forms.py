from django import forms
from .models import HiQGallery

class galform(forms.ModelForm):
    class Meta:
        model = HiQGallery
        fields = ("imagedescription","image")
