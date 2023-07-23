from django import forms

from book.models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'price')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light mb-2',
                'placeholder': 'Enter book title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light mb-2',
                'placeholder': 'Enter author full name'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-light mb-2',
                'placeholder': 'Enter year'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-light mb-2',
                'placeholder': 'Enter price'
            })
        }
