# Generated by Django 4.2.6 on 2023-11-12 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restoran',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='restoran',
            name='long',
        ),
    ]
