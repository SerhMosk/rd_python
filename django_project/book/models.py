from django.db import models
from user.models import User


class Book(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    year = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    users = models.ManyToManyField(User, related_name='books')

    def __str__(self):
        return f'{self.id}: {self.title} - {self.author}'

    class Meta:
        db_table = 'book'
        unique_together = (('title', 'author'),)
