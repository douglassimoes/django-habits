from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserCreationForm
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
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = hash(request.POST.get('password1'))
            
            user = models.User(username=username,email=email,password=password)
            user.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'habits/signup.html', context)

def login(request):
    if request.method == 'POST':
        print(request.POST.keys())
        form = UserCreationForm(request.POST)
        dir(form.data)
        for field in form:
            print("Field Error {} {}".format(field.name, field.errors))
        if form.is_valid():
            email = request.POST.get('email')
            password = hash(request.POST.get('password1'))
            try:
                user = User.objects.get(username=username,email=email,password=password)
                return render(request, 'habits/dashboard.html',{user_id: user.id})
            except User.DoesNotExist:
                messages.error(request, f'Wrong email or password.')    
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'habits/login.html', context)

def dashboard(request, pk):
    return render(request, 'habits/dashboard.html',{})


def allhabits(request):
    return render(request, 'habits/dashboard.html',{})

def createhabit(request):
    if request.method == 'POST':
        print(request.POST.keys())
        habitname = request.POST.get('habitname')
        description = request.POST.get('description')
        category = hash(request.POST.get('category'))
        repetition = hash(request.POST.get('repetition'))
        habit = models.Habit(habitname=habitname,description=description,category=category,repetition=repetition)
        habit.save()
    return render(request, 'habits/createhabit.html',{})

def scorecard(request):
    return render(request, 'habits/dashboard.html',{})