from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact.models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )
    

    # first_name = forms.CharField(
    #     widget= forms.PasswordInput(
    #         attrs={
    #             'placeholder': 'Alterando propriedades de first_name',
    #         }
    #     ),
    #     # label= 'Senha'
    # )

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
                field='first_name',
                error='ValidationError'
            )

    
        