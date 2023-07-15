from django.db import models
from book.models import Book
from user.models import User


class Purchase(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    book = models.ForeignKey(Book, related_name='purchases', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False)

    class Meta:
        db_table = 'purchase'
        ordering = ('-created_at',)
