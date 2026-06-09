from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'form-input',
        }),
        error_messages={
            'required': 'This field is required',
        },
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class': 'form-input',
        }),
        error_messages={
            'required': 'This field is required',
        },
    )
