from django import forms
from django.forms import ModelForm
from .models import Profile

STATE = [
    ('Abia', 'Abia'),
    ('Bayelsa', 'Bayelsa'),
    ('Ekiti', 'Ekiti'),
    ('Ondo', 'Ondo'),
    ('Lagos', 'Lagos'),
    ('Kano', 'Kano'),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'state', 'profile_pix']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name is required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Nmae is required'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email is required'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.Select(attrs={'class': 'form-control', 'placeholder': 'State is required'},choices=STATE),
            'profile_pix': forms.FileInput(attrs={'class': 'form-control'}),
        }