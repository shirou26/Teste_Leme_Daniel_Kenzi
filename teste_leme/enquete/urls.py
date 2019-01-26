from django.urls import path
from . import views

app_name = 'enquete'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('', views.retornar, name='retornar'),
    path('resultado/', views.resultado, name='resultado'),
]
