# Generated by Django 4.2.4 on 2023-08-12 11:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('year', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('price', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'db_table': 'book',
                'ordering': ['id'],
            },
        ),
    ]
