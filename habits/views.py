from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from habits import models
import re

# Create your views here.
def home(request):
    return render(request, 'habits/index.html', {})

def signup(request):
    if request.method == 'POST':
        print(request.POST.keys())
        form = UserCreationForm(request.POST)
        dir(form.data)
        for field in form:
            print("Field Error {} {}".format(field.name, field.errors))
        if form.is_valid():
            print("Form valid")
            user = form.save()
            user.set_password(user.password)
            user.email = request.POST.get('email')
            user.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'habits/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        print(request.POST.keys())
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'habits/login.html', {})

@login_required
def dashboard(request):
    return render(request, 'habits/dashboard.html',{"user_id": request.user.pk})

@login_required
def allhabits(request):
    habitlist = models.Habit.objects.filter(user_id=request.user)
    print(habitlist)
    return render(request, 'habits/allhabits.html',{"habits": habitlist})

@login_required
def createhabit(request):
    if request.method == 'POST':
        print(request.POST.keys())
        habitname = request.POST.get('habitname')
        description = request.POST.get('description')
        category = request.POST.getlist('category')[0]
        repetition = request.POST.getlist('repetition')[0]
        color = request.POST.getlist('color')[0]
        habit = models.Habit(user_id=request.user,habitname=habitname,description=description,category=str(category),repetition=str(repetition),color=color)
        habit.save()
        tracker = models.Tracker(user_id=request.user,habit_id=habit,duration=0)
        tracker.save()
    return render(request, 'habits/createhabit.html',{})

@login_required
def scorecard(request):
    habitlist = models.ScorecardHabit.objects.filter(user_id=request.user)
    if request.method == 'POST':
        print(request.POST.keys())
        regex = re.compile("remove.*")
        match_answer = list(filter(regex.match, request.POST.keys()))
        if  match_answer:
            habit_to_remove = match_answer[0].split(":")[1]
            scorecard_habit = models.ScorecardHabit.objects.filter(id=str(habit_to_remove))
            scorecard_habit.delete()
            render(request, 'habits/scorecard.html',{"scorecard_habits": habitlist})
        else: 
            habitname = request.POST.get('habitname')
            schedule = request.POST.getlist('schedule')[0]
            score = request.POST.getlist('score')[0]
            scorecard_habit = models.ScorecardHabit(user_id=request.user,habitname=habitname,schedule=str(schedule),score=str(score))
            scorecard_habit.save()
    return render(request, 'habits/scorecard.html',{"scorecard_habits": habitlist})

@login_required
def loghabit(request):
    print("dale")
    habitlist = models.Habit.objects.filter(user_id=request.user)
    print(habitlist)
    if request.method == 'POST':
        print(request.POST.keys())
        log = request.POST.get('log')
        regex = re.compile("log.*")
        match_answer = list(filter(regex.match, request.POST.keys()))
        print(log)
    return render(request, 'habits/loghabit.html',{"habits": habitlist})