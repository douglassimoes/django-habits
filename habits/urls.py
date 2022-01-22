from django.urls import path
from habits import views

urlpatterns = [
    path('', views.home, name='home'),
]