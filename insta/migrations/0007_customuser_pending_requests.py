# Generated by Django 3.2.5 on 2021-07-27 15:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0006_rename_public_acc_customuser_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='pending_requests',
            field=models.ManyToManyField(blank=True, related_name='private_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
