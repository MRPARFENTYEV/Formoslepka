from django import forms
from accounts.models import Address, User


class Admin_user_address_data_form(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'street', 'house', 'structure', 'building', 'apartment']
        widgets = {'city': forms.TextInput(attrs={'placeholder': 'Город'}),
                   'street': forms.TextInput(attrs={'placeholder': 'Улица'}),
                   'house': forms.TextInput(attrs={'placeholder': 'Дом'}),
                   'structure': forms.TextInput(attrs={'placeholder': 'Строение'}),
                   'building': forms.TextInput(attrs={'placeholder': 'Здание'}),
                   'apartment': forms.TextInput(attrs={'placeholder': 'Квартира'})}




