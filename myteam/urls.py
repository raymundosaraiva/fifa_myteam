from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('initialdata', views.import_csv, name='import_csv'),
    path('get_team', views.get_team, name='team'),
]
