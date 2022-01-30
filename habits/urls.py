from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('createhabit/', views.createhabit, name='createhabit'),
    path('loghabit/', views.loghabit, name='loghabit'),
    path('allhabits/', views.allhabits, name='allhabits'),
    path('scorecard/', views.scorecard, name='scorecard')
]