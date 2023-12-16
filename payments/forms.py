# forms.py
from django import forms
from .models import UserWallet

class CreateWalletForm(forms.ModelForm):
    class Meta:
        model = UserWallet
        fields = ['currency']
