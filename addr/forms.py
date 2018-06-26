from django import forms

from .models import Address, AddrMemo


class AddrForm(forms.ModelForm):

    class Meta :
        model = Address
        fields = ('name', 'num', 'num2', 'email',)


class MemoForm(forms.ModelForm):

    class Meta:
        model = AddrMemo
        fields = ('author', 'text',)
