from django.urls import path
from . import views

urlpatterns = [
    path('mensajes/recibidos/', views.ver_mensajes_recibidos, name='ver_mensajes_recibidos'),
]
