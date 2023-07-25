from django import forms

from purchase.models import Purchase


class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = ('book', 'user')

        widgets = {
            'book': forms.Select(attrs={
                'class': 'form-select bg-dark text-light mb-2',
                'placeholder': 'Select book'
            }),
            'user': forms.Select(attrs={
                'class': 'form-select bg-dark text-light mb-2',
                'placeholder': 'Select user'
            })
        }
