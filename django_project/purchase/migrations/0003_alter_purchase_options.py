# Generated by Django 4.2.3 on 2023-07-15 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ('-created_at',)},
        ),
    ]
