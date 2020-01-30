from django.forms import ModelForm
from .models import suggetionbox



class sugfrm(ModelForm):
    class Meta:
        model = suggetionbox
        fields = ("suggcontent",)



        # widgets = {
        # "suggcontent":"textarea",
        #
        #
        #
        # }
