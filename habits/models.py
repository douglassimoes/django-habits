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
    
    class HabitColor(models.TextChoices):
        BG_primary = "bg-primary"
        BG_secondary = "bg-secondary"
        BG_success = "bg-success"
        BG_danger = "bg-danger"
        BG_warning = "bg-warning"
        BG_info = "bg-info" 
    
    class HabitRepetition(models.TextChoices):
        Everyday = "Everyday"
        OnceAWeek = "OnceAWeek"
    
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    habitname = models.CharField(max_length=254, default="")
    description = models.CharField(max_length=254, default="")
    start_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=254,choices=HabitCategories.choices, default="")
    repetition = models.CharField(max_length=254,choices=HabitRepetition.choices, default="")
    color = models.CharField(max_length=254,choices=HabitColor.choices, default="")

class ScorecardHabit(models.Model):
    class Scores(models.TextChoices):
        POSITIVE = "+"
        NEUTRAL = "="
        NEGATIVE = "-"
    
    class Schedules(models.TextChoices):
        BEFORE_NOON = "6am-12pm"
        AFTERNOON = "12-6pm"
        EVENING = "6pm-12am"
    
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    habitname = models.CharField(max_length=254, default="")
    schedule = models.CharField(max_length=254,choices=Schedules.choices, default="")
    score = models.CharField(max_length=254,choices=Scores.choices, default="")

class Tracker(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    habit_id = models.ForeignKey(Habit, on_delete = models.CASCADE)
    actual_date = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField()