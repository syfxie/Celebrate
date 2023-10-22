# Generated by Django 4.1 on 2023-10-22 02:21

import birthYay.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=30)),
                ('birthday', models.DateField(validators=[birthYay.models.validate_date_in_past])),
                ('followers', models.ManyToManyField(related_name='following', to='birthYay.user')),
            ],
        ),
    ]
