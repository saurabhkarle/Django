from django.urls import path
from . import views

urlpatterns = [
    path('sayworld/', views.say_world),
    path('world/', views.world)
]