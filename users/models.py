from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from app_drf.models import Course, Lesson
from django.utils import timezone

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='Город')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватарка')

    USERNAME_FIELD = 'email'  # Указываем, что авторизация будет по email
    REQUIRED_FIELDS = []  # Убираем username из обязательных полей

    def __str__(self):
        return self.email


class Payments(models.Model):
    PAYMENTS_METHOD = [
        ("cash", "Наличные"),
        ("transfer", "Перевод на счёт")
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    payment_date = models.DateTimeField(default=timezone.now, verbose_name="Дата оплаты")
    course = models.ForeignKey('app_drf.Course', on_delete=models.CASCADE, **NULLABLE, verbose_name="Курс")
    lesson = models.ForeignKey('app_drf.Lesson', on_delete=models.CASCADE, **NULLABLE, verbose_name="Урок")
    payments_method = models.CharField(max_length=10, choices=PAYMENTS_METHOD, verbose_name="Способ оплаты")
    summ_payment = models.PositiveIntegerField(verbose_name="Сумма оплаты")

    def __str__(self):
        return f"{self.user.email} - {self.summ_payment} - {self.payments_method} - {'Курс: ' + str(self.course) if self.course else ''}{' Урок: ' + str(self.lesson) if self.lesson else ''}"
