# Generated by Django 4.1.6 on 2023-06-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
