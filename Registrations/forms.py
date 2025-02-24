from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        exclude = ('event',)
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'company_address': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'fax_number': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'website': forms.URLInput(attrs={'class': 'form-control mb-3'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'contact_person_telephone_number': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'managing_director': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'managing_director_telephone_number': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'managing_director_email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'products': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 3}),
            'services': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 3}),
        }
