from django.shortcuts import render
from .models import Mensaje
from django.http import HttpRequest

# Create your views here.

def ver_mensajes_recibidos(request):
    mensajes_todos = Mensaje.objects.all()  # Obtener todos los mensajes inicialmente

    remitente = request.GET.get('mensaje_remitente')
    mensajes_remitente = mensajes_todos
    if remitente:
        mensajes_remitente = mensajes_remitente.filter(remitente=remitente)

    destinatario = request.GET.get('mensaje_destinatario')
    mensajes_destinatario = mensajes_todos
    if destinatario:
        mensajes_destinatario = mensajes_destinatario.filter(destinatario=destinatario)

    return render(request, 'recibido.html', {
        'mensajes_remitente': mensajes_remitente,
        'mensajes_destinatario': mensajes_destinatario
    })
