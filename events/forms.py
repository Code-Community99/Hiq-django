from django import forms
from .models import events_list


class eventfrm(forms.ModelForm):
    class Meta:
        model = events_list
        fields = ["event_description"]
