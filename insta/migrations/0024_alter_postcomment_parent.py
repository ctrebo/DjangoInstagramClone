# Generated by Django 3.2.5 on 2021-11-19 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0023_alter_postcomment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='insta.postcomment'),
        ),
    ]
