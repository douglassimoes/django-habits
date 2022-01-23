from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    
    class HabitRepetition(models.TextChoices):
        Everyday = "Everyday"
        OnceAWeek = "OnceAWeek"
    
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    habitname = models.CharField(max_length=254, default="")
    description = models.CharField(max_length=254, default="")
    start_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=254,choices=HabitCategories.choices, default="")
    repetition = models.CharField(max_length=254,choices=HabitRepetition.choices, default="")

class Tracker(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    habit_id = models.ForeignKey(Habit, on_delete = models.CASCADE)
    actual_date = models.DateField()
    duration = models.PositiveIntegerField()