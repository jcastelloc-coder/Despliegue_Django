from django.shortcuts import render
def index(request):
    context = {
        'titulo': 'Demostracion de Django-Unemi',
        'mensaje':'Este mensaje proviene del diccionario de contexto en views.py.'
    }
    return render(request,'mi_app/index.html',context)
# Create your views here.
