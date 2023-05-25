from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Модель пользователя
    """

    class UserRole(models.TextChoices):
        CLIENT = "client", _("Клиент")
        INSPECTOR = "inspector", _("Инспектор")

    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128, null=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(
        choices=UserRole.choices,
        max_length=10,
        blank=True,
        default=UserRole.CLIENT,
        verbose_name="Роль пользователя",
    )

    class Meta:
        managed = False
        db_table = "users_user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
