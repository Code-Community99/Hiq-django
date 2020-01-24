from django import forms
from .models import project


class uploadform(forms.ModelForm):
    # category = forms.ChoiceField(options=["It"])
    class Meta:
        model = project
        fields = ["category" , "project_name" , "project_description" , "file"]
