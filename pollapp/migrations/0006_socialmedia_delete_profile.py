# Generated by Django 4.1.6 on 2023-06-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0005_profile_email_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin_url', models.URLField()),
                ('email_url', models.URLField()),
                ('github_url', models.URLField()),
                ('instagram_url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
