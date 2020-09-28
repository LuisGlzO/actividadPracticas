from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm


# Create your views here.

def inicio(request):#esta funcion recibe una peticion del navegador, será request
    personas = Persona.objects.all() #Para hacer una consulta
    ##print(personas)
    contexto = {
        'personas':personas
    }
    return render(request,'index.html',contexto)
    #Ahora hay que crear una ruta para que pinte el template

def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto ={
            'form':form 
        }
    else:
        form = PersonaForm(request.POST)
        contexto ={
            'form':form 
        }
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request,'crear_persona.html',contexto)

def editarPersona(request, id):
    persona = Persona.objects.get(id = id)
    #viene la accion
    if request.method == 'GET':
        form = PersonaForm(instance = persona)
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST, instance=persona)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_persona.html', contexto)
    
    return render(request,'crear_persona.html',contexto)

def eliminarPersona(request, id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')