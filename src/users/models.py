from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    country = models.CharField(blank=True, max_length=128)
    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(120)]
    )

    def __str__(self):
        return self.username
