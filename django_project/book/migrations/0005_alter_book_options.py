# Generated by Django 4.2.3 on 2023-07-31 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_price_alter_book_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['id']},
        ),
    ]
