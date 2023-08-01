from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser):
    id = models.IntegerField(unique=True, primary_key=True)
    username = models.CharField(max_length=20, unique=True, null=False)
    first_name = models.CharField(max_length=255, unique=True, null=False)
    last_name = models.CharField(max_length=255, unique=True, null=False)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(6)]
    )
    password = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.id}: {self.username}'

    class Meta:
        db_table = 'user'
        ordering = ['id']
