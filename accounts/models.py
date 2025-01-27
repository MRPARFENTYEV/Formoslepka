from datetime import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.urls import reverse
from django.utils.timezone import now
from rest_framework.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, patronym=None):
        if not email:
            raise ValidationError({'email': 'Email is required!'})
        if not first_name:
            raise ValidationError({'first_name': 'First name is required!'})
        if not last_name:
            raise ValidationError({'last_name': 'Last name is required!'})
        if not password:
            raise ValidationError({'password': 'Password is required!'})

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            patronym=patronym
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, patronym=None):
        user = self.create_user(email, first_name, last_name, password, patronym)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    patronym = models.CharField(max_length=100, verbose_name='Отчество', blank=True, null=True)  # null=True убран
    date_joined = models.DateTimeField(default=now)
    image = models.ImageField(upload_to='accounts')
    birthday_date = models.DateField(max_length=10, verbose_name='Дата рождения', blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, unique=True, verbose_name='Электронная почта', blank=False, null=False)
    position = models.CharField(max_length=100, unique=True, verbose_name='Должность', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('accounts:user_detail', kwargs={'user_id': self.id})
    # Добавьте эти методы:
    def has_perm(self, perm, obj=None):
        """
        Проверка конкретного разрешения.
        Обычно возвращает True для суперпользователей.
        """
        return self.is_admin

    def has_module_perms(self, app_label):
        """
        Проверяет доступ пользователя к приложению (модулю).
        """
        return self.is_admin

    def __str__(self):
        return self.email


class Contact(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='contacts', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    telegram = models.CharField(max_length=50, verbose_name='Телеграм')

    class Meta:
        verbose_name = 'Контакты пользователя'
        verbose_name_plural = 'Список контактов пользователя'

    def __str__(self):
        return f'{self.user} {self.phone} {self.telegram} '


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='adresses', on_delete=models.CASCADE)
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=15, verbose_name='Дом', blank=True, null=True, )
    structure = models.CharField(max_length=15, verbose_name='Корпус', blank=True, null=True, )
    building = models.CharField(max_length=15, verbose_name='Строение', blank=True, null=True, )
    apartment = models.CharField(max_length=15, verbose_name='Квартира', blank=True, null=True, )

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.city} {self.street} {self.house} {self.apartment} {self.phone} {self.user}'


class Military_service(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='military_service',
                             on_delete=models.CASCADE)
    gd = models.CharField(max_length=7, verbose_name='ГД', blank=True, null=True)
    personal_number = models.CharField(max_length=10, verbose_name='Личный номер', blank=True, null=True)
    released = models.CharField(max_length=100, verbose_name='Выдан', blank=True, null=True)
    release_data_day = models.CharField(max_length=2, verbose_name='День выдачи', blank=True, null=True)
    release_data_month = models.CharField(max_length=2, verbose_name='Месяц выдачи', blank=True, null=True)
    release_data_year = models.CharField(max_length=4, verbose_name='Год выдачи', blank=True, null=True)
    rank = models.CharField(max_length=50, verbose_name='Воинское звание', blank=True, null=True)
    order = models.CharField(max_length=100, verbose_name='Присвоено приказом', blank=True, null=True)
    military_specialty = models.CharField(max_length=10, verbose_name='ВУС №', blank=True, null=True)
    profile_name = models.CharField(max_length=10, verbose_name='Наименование профиля', blank=True, null=True)
    reserve_num = models.CharField(max_length=10, verbose_name='Разряд запаса', blank=True, null=True)
    mil_service = models.CharField(max_length=10, verbose_name='Проходил службу с... по...', blank=True, null=True)
    pinned = models.CharField(max_length=10, verbose_name='Прикреплен или снят с учета', blank=True, null=True)

    class Meta:

        verbose_name = 'Военный билет'
        verbose_name_plural = 'Военные билеты'

    def __str__(self):
        return (f'{self.user} {self.personal_number} {self.released} {self.personal_number} {self.released} '
                f'{self.release_data_day}, {self.release_data_month},{self.release_data_year}')


class Passport(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='passports', on_delete=models.CASCADE)
    passport_serial_number = models.CharField(max_length=4, verbose_name='Серия', blank=True, null=True)
    passport_num = models.CharField(max_length=6, verbose_name='Номер паспорта', blank=True, null=True)
    released = models.CharField(max_length=200, verbose_name='Выдан', blank=True, null=True)
    released_data = models.CharField(max_length=10, verbose_name='Дата выдачи', blank=True, null=True)
    department_code = models.CharField(max_length=10, verbose_name='Код подразделения', blank=True, null=True)

    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'

    def __str__(self):
        return f'{self.passport_serial_number} {self.passport_num} {self.released}'


class Diploma(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='diplomas', on_delete=models.CASCADE)
    organisation = models.CharField(max_length=250, verbose_name='Организация', blank=True, null=True)
    education_level = models.CharField(max_length=15, verbose_name='Уровень образования', blank=True, null=True)
    serial_number = models.CharField(max_length=10, verbose_name='Номер диплома', blank=True, null=True)
    register_number = models.CharField(max_length=10, verbose_name='Регистрационный номер', blank=True, null=True)
    speciality = models.CharField(max_length=50, verbose_name='Специальность')
    class Meta:
        verbose_name = 'Диплом'
        verbose_name_plural = 'Дипломы'

    def __str__(self):
        return f'{self.speciality}'
