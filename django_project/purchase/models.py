from django.db import models
from book.models import Book
from user.models import User


class Purchase(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    book = models.ForeignKey(Book, related_name='purchases', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return f'{self.id}: book_id: {self.book_id}, user_id: {self.user_id}'

    class Meta:
        db_table = 'purchase'
        ordering = ('-created_at',)
