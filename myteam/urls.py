from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_team', views.get_team, name='team'),
]
