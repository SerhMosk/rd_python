from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

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


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'username':
                field.widget.attrs['class'] = 'form-control bg-dark text-light mb-2'
                field.widget.attrs['placeholder'] = 'Enter username'
            elif field_name == 'password1':
                field.widget.attrs['class'] = 'form-control bg-dark text-light mb-2'
                field.widget.attrs['placeholder'] = 'Enter password'
            elif field_name == 'password2':
                field.widget.attrs['class'] = 'form-control bg-dark text-light mb-2'
                field.widget.attrs['placeholder'] = 'Confirm password'
            elif field_name == 'email':
                field.widget.attrs['class'] = 'form-control bg-dark text-light mb-2'
                field.widget.attrs['placeholder'] = 'Enter email'
            elif field_name == 'first_name':
                field.widget.attrs['class'] = 'form-control bg-dark text-light mb-2'
                field.widget.attrs['placeholder'] = 'Enter first name'
            elif field_name == 'last_name':
                field.widget.attrs['class'] = 'form-control bg-dark text-light mb-2'
                field.widget.attrs['placeholder'] = 'Enter last name'
            elif field_name == 'age':
                field.widget.attrs['class'] = 'form-control bg-dark text-light mb-2'
                field.widget.attrs['placeholder'] = 'Enter age'

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'age',
            'is_superuser',
            'is_staff',
            'is_active'
        )  # if you want to add more fields
