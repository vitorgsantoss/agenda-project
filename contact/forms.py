from contact.models import Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm
from contact.models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):

    # Fazendo com que os campos abaixo se tornem obrigatórios
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()


    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Este e-mail já está cadastrado', code='invalid')
            )

        return email

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget= forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        )


    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
                field='first_name',
                error='ValidationError'
            )

    
        