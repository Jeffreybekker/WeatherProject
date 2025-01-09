from django.urls import path
from . import views

urlpatterns = [
    path('weather-forecast',views.index, name='index')
]
