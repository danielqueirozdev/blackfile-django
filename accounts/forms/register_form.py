from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


def strong_password(password):
    regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(
            'Weak password. Your password must have: at least 8 characters, '
            'one uppercase letter and one lowercase letter.'
        )


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
        }
        error_messages = {
            'username': {
                'required': 'This field is required',
            },
            'email': {
                'required': 'This field is required',
            },
            'password': {
                'required': 'This field is required',
            },
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Your username',
                'class': 'form-input',
            }),
        }

    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your email address',
            'class': 'form-input',
        }),
        error_messages={
            'required': 'This field is required',
        },
    )

    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class': 'form-input',
        }),
        validators=[strong_password],
        error_messages={
            'required': 'This field is required',
        },
    )

    confirm_password = forms.CharField(
        required=True,
        label='Confirm password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password',
            'class': 'form-input',
        }),
        error_messages={
            'required': 'This field is required',
        },
    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            return email

        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('This email is already in use')

        return email
