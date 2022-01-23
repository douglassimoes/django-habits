from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from habits import models

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
    return render(request, 'habits/dashboard.html',{"user_id": request.user.pk})

@login_required
def createhabit(request):
    if request.method == 'POST':
        print(request.POST.keys())
        habitname = request.POST.get('habitname')
        description = request.POST.get('description')
        category = request.POST.getlist('category')[0]
        repetition = request.POST.getlist('repetition')[0]
        habit = models.Habit(user_id=request.user,habitname=habitname,description=description,category=str(category),repetition=str(repetition))
        habit.save()
    return render(request, 'habits/createhabit.html',{})

def scorecard(request):
    return render(request, 'habits/dashboard.html',{})