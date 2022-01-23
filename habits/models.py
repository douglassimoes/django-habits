from django.db import models

# Create your models here.
# the PK is automatically created by Django
class User(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, default="john@doe.com")
    password = models.CharField(max_length=50, default="1234")

class Habit(models.Model):
    class HabitCategories(models.TextChoices):
        Reading = "Reading"
        Exercise = "Exercise"
        Practicing_Music = "Practicing Music"
        Writing = "Writing"
        Language_Learning = "Language Learning"
        Savings = "Savings"
        Gratitude = "Gratitude"
        Productivity = "Productivity"
        Relationships = "Relationships"
        Healthy_Eating = "Healthy Eating"
        Parenting = "Parenting"
        Meditation = "Meditation" 
    
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    habitname = models.CharField(max_length=254, default="")
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.CharField(max_length=254,choices=HabitCategories.choices)
    repetition = models.TextChoices('Everyday','OnceAWeek')

class Tracker(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    habit_id = models.ForeignKey(Habit, on_delete = models.CASCADE)
    actual_date = models.DateField()
    duration = models.PositiveIntegerField()