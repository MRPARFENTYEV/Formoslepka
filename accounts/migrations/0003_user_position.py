# Generated by Django 5.1.3 on 2024-12-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_patronym'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='Должность'),
        ),
    ]
