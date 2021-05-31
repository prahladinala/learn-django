from django.urls import path
from . import views

urlpatterns = [
    path('prahlad', views.index),
    path('febrauary', views.february)
]
