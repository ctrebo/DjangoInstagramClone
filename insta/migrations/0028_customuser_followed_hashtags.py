# Generated by Django 3.2.5 on 2022-01-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0027_hashtag_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='followed_hashtags',
            field=models.ManyToManyField(blank=True, related_name='followed_field_hashtag', to='insta.Hashtag'),
        ),
    ]
