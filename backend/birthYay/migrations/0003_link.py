# Generated by Django 4.1 on 2023-10-31 02:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('birthYay', '0002_alter_customuser_email_gift'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gift', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='birthYay.gift')),
            ],
        ),
    ]
