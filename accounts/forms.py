from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from .models import User, Address, Military_service, Contact, Diploma, Passport


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


class EditUserForm(forms.ModelForm):
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


class MilitaryServiceForm(forms.ModelForm):
    class Meta:
        model = Military_service
        fields = ['gd', 'personal_number', 'released', 'release_data_day', 'release_data_month',
                  'release_data_year','rank','order','military_specialty','profile_name','reserve_num',
                  'mil_service','pinned']

        widgets = {'gd': forms.TextInput(attrs={'placeholder': 'Указывается сверху - "ГД"'}),
                   'personal_number': forms.TextInput(attrs={'placeholder': 'Персональный номер'}),
                   'released': forms.TextInput(attrs={'placeholder': 'Выдан'}),
                   'release_data_day': forms.TextInput(attrs={'placeholder': 'День выдачи'}),
                   'release_data_month': forms.TextInput(attrs={'placeholder': 'Месяц выдачи'}),
                   'release_data_year': forms.TextInput(attrs={'placeholder': 'Год выдачи'}),
                   'rank': forms.TextInput(attrs={'placeholder': 'Воинское звание'}),
                   'order': forms.TextInput(attrs={'placeholder': 'Присвоено приказом'}),
                   'military_specialty': forms.TextInput(attrs={'placeholder': 'Приказом'}),
                   'profile_name': forms.TextInput(attrs={'placeholder': 'Командный профиль'}),
                   'reserve_num': forms.TextInput(attrs={'placeholder': 'Разряд резерва'}),
                   'mil_service': forms.TextInput(attrs={'placeholder': 'Службу прошел'}),
                   'pinned': forms.TextInput(attrs={'placeholder': 'Прикреплен к военкомату'})

                   }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['phone','telegram']
        widgets = {'phone': forms.TextInput(attrs={'placeholder': 'формат: 89160001122'}),
                   'telegram': forms.TextInput(attrs={'placeholder': 'формат: @your tg account`s title'})}

class DiplopmaForm(forms.ModelForm):
    class Meta:
        model = Diploma
        fields = ['organisation', 'education_level','serial_number','register_number','speciality']

        widgets = {'organisation': forms.TextInput(attrs={'placeholder': 'Самый лучший вуз, о котором никто не слышал'}),
                   'education_level': forms.TextInput(attrs={'placeholder': 'Отец отечества'}),
                   'serial_number': forms.TextInput(attrs={'placeholder': '123'}),
                   'register_number': forms.TextInput(attrs={'placeholder': '456'}),
                   'speciality': forms.TextInput(attrs={'placeholder': 'слесарь'}),

                   }
class PassportForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = ['passport_serial_number', 'passport_num', 'released', 'released_data', 'department_code']

        # widgets = {
        #     'passport_serial_number': forms.TextInput(attrs={'placeholder': '123'}),
        #     'passport_num': forms.TextInput(attrs={'placeholder': '456'}),
        #     'released': forms.TextInput(attrs={'placeholder': ''}),
        #     'released_data': forms.TextInput(attrs={'placeholder': '456'}),
        #     'department_code': forms.TextInput(attrs={'placeholder': 'слесарь'}),
        #
        #     }
