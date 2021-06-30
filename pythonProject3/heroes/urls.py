from django.urls import path
from . import views

app_name = 'heroes'
urlpatterns = [
    path('', views.index, name='index')
]