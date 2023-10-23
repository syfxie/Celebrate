# Generated by Django 4.1 on 2023-10-23 01:01

import birthYay.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthYay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[birthYay.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='message',
            field=models.CharField(blank=True, default='Have a peek!', max_length=254, null=True),
        ),
    ]