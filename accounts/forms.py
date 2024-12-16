from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from .models import User, Address


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Почта'}
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Имя'}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Фамилия'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Пароль'}
        )
    )


class EditUserForm(forms.Form):
    class Meta:
        model = User
        fields = ['position', 'first_name', 'last_name', 'patronym', 'email', 'birthday_date', ]
        widgets = {'position': forms.TextInput(attrs={'placeholder': 'Должность'}),
                   'first_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
                   'patronym': forms.TextInput(attrs={'placeholder': 'Отчество'}),
                   'birthday_date': forms.TextInput(attrs={'placeholder': 'Дата рождения'}),
                   # 'image': forms.ImageField(attrs={'placeholder': 'Аватарка'}),
                   'email': forms.TextInput(attrs={'placeholder': 'Пример: User@mail.ru'})}

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










class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'почта'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'пароль'}
        )
    )