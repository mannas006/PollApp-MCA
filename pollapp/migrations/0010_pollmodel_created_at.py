# Generated by Django 4.1.6 on 2023-06-12 12:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0009_remove_socialmedia_email_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollmodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]