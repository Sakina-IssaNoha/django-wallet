from dataclasses import fields
from pyexpat import model
from django import forms
from ...wallet.models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"