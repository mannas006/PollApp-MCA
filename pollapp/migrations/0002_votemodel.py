# Generated by Django 4.1.6 on 2023-06-02 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteModel',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('vote', models.CharField(max_length=40)),
            ],
        ),
    ]