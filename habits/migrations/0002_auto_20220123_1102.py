# Generated by Django 3.2.5 on 2022-01-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='imagepath',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='john@doe.com', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='1234', max_length=50),
        ),
    ]
