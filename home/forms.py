from django import forms
from .models import home_data

# class loginfrm(forms.ModelForm):
#     class Meta:
#         model = "hqlog"
#         fields = [""]


class loginfrm(forms.Form):
    username = forms.CharField(max_length = 40 ,label = "hq")
    password = forms.CharField(max_length = 40 ,label = "hq")
    email = forms.CharField(max_length = 40 ,label = "hq")
