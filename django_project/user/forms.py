from django import forms

from user.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'age',
            'is_superuser',
            'is_staff',
            'is_active'
        )

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light mb-2',
                'placeholder': 'Enter username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-dark text-light mb-2',
                'placeholder': 'Enter email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control bg-dark text-light mb-2',
                'placeholder': 'Enter password'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light mb-2',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light mb-2',
                'placeholder': 'Enter last name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-light mb-2',
                'placeholder': 'Enter age'
            }),
            'is_superuser': forms.CheckboxInput(attrs={}),
            'is_staff': forms.CheckboxInput(attrs={}),
            'is_active': forms.CheckboxInput(attrs={})
        }
