# Generated by Django 3.2.5 on 2021-08-17 12:14

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0011_story'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelManagers(
            name='story',
            managers=[
                ('active_story_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
