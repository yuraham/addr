from django import forms

from .models import Address


class AddrForm(forms.ModelForm):

    class Meta :
        model = Address
        fields = ('name', 'num', 'num2', 'email',)

