from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

NULLABLE = {
    'null': True,
    'blank': True
}


class User(AbstractUser):
    username = None
    phone = models.CharField(unique=True, verbose_name='телефон')
    first_name = models.CharField(verbose_name='имя', max_length=50)
    last_name = models.CharField(verbose_name='фамилия', max_length=50)
    city = models.CharField(verbose_name='населенный пункт', max_length=150)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class CompanyCard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                             **NULLABLE)
    type = models.CharField(verbose_name='тип организации', max_length=150, **NULLABLE)
    bank_account = models.CharField(verbose_name='банковские реквизиты', max_length=150, **NULLABLE)
    INN = models.CharField(verbose_name='Свидетельство ИНН', max_length=150, unique=True, **NULLABLE)
    ogrn = models.CharField(verbose_name='Свидетельство ОГРН (для ИП ОГРНИП)', max_length=150, unique=True, **NULLABLE)
    guid = models.CharField(verbose_name='код GUID', max_length=150, unique=True, **NULLABLE)

    class Meta:
        verbose_name = 'карточка компании'
        verbose_name_plural = 'карточки компании'
