from django.forms import ModelForm ,Textarea
from .models import suggetion_box



class sugfrm(ModelForm):
    class Meta:
        model = suggetion_box
        widgets = {
        'suggestion':Textarea(attrs = {"rows":6 , "cols":40})
        }
        fields = ("suggestion",)



        # widgets = {
        # "suggcontent":"textarea",
        #
        #
        #
        # }
