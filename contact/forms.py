from contact.models import Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from contact.models import User
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget= forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
            
        ),
        required=False
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
    

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
)

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('As senhas devem ser iguais.')
                )

        return super().clean()
    
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password= cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        print(f'Email:{email}')
        print(f'Current email: {current_email}')

        if current_email == email:
            return email
        
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            self.add_error(
                'email',
                ValidationError('Este e-mail já está cadastrado', code='invalid')
            )

        return email
    
    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if password:
            try:
                password_validation.validate_password(password)

            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password

   