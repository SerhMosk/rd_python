from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse_lazy

from user.models import User


class Book(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )
    price = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )
    users = models.ManyToManyField(User, related_name='books')

    def __str__(self):
        return f'{self.id}: {self.title} - {self.author}'

    def get_absolute_url(self):
        return reverse_lazy('books:book-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'book'
        unique_together = (('title', 'author'),)
        ordering = ['id']
