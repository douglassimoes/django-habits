# Generated by Django 3.2.5 on 2022-01-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0007_auto_20220123_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='description',
            field=models.CharField(default='', max_length=254),
        ),
    ]
