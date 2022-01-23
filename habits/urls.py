from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('dashboard/<int:pk>/', views.dashboard, name='dashboard'),
    path('createhabit/', views.createhabit, name='createhabit'),
    path('allhabits/', views.allhabits, name='allhabits'),
    path('scorecard/', views.scorecard, name='scorecard')
]