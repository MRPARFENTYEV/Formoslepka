from datetime import timezone

from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.urls import reverse
from django.utils.timezone import now
from rest_framework.exceptions import ValidationError

class UserManager(BaseUserManager):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    patronym = models.CharField(max_length=100, verbose_name='Отчество')
    date_joined = models.DateTimeField(default=now)
    image = models.ImageField(upload_to='users')
    # is_admin = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=100, unique=True, verbose_name='Электронная почта')

    def create_user(self, email, first_name, last_name, password, patronym=None):
        if not email:
            raise ValidationError({'email': 'Email is required!'})
        if not first_name:
            raise ValidationError({'first_name': 'first_name is required!'})
        if not last_name:
            raise ValidationError({'last_name': 'last_name is required!'})
        if not password:
            raise ValidationError({'password': 'password is required'})

        user = self.model(email=self.normalize_email(email), first_name=self.first_name, last_name=self.last_name)
        user.set_password(password)
        user.save(using=self.db)
        return user