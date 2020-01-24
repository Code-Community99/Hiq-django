from django import forms
from signup.models import signup_user

class loginfrm(forms.ModelForm):
    class Meta:
        model = signup_user
        fields = ("First_Name" , "Second_name" , "Password" , "Email" ,"Phone_Number")
