# Generated by Django 3.2.5 on 2021-11-18 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0022_auto_20211111_1635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcomment',
            options={'ordering': ['post_date']},
        ),
    ]
