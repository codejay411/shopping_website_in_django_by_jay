# Generated by Django 3.0.5 on 2020-05-12 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200513_0249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
    ]
