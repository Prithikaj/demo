
from django import forms
from .models import Contactt

class ContacttForm(forms.ModelForm):

    class Meta:
        model = Contactt
        fields = ['name', 'phone']
