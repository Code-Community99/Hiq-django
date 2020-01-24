from django import forms
from .models import comment_list

class commentform(forms.ModelForm):
    class Meta:
        model = comment_list
        fields = ["comments"]
