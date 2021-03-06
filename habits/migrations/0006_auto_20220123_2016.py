# Generated by Django 3.2.5 on 2022-01-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_auto_20220123_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='repetition',
            field=models.CharField(choices=[('Everyday', 'Everyday'), ('OnceAWeek', 'Onceaweek')], default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='habit',
            name='category',
            field=models.CharField(choices=[('Reading', 'Reading'), ('Exercise', 'Exercise'), ('Practicing Music', 'Practicing Music'), ('Writing', 'Writing'), ('Language Learning', 'Language Learning'), ('Savings', 'Savings'), ('Gratitude', 'Gratitude'), ('Productivity', 'Productivity'), ('Relationships', 'Relationships'), ('Healthy Eating', 'Healthy Eating'), ('Parenting', 'Parenting'), ('Meditation', 'Meditation')], default='', max_length=254),
        ),
    ]
