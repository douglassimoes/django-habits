# Generated by Django 3.2.5 on 2022-01-23 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_habit_habitname'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='habits.user'),
        ),
    ]