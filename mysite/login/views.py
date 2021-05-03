from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario {username} ha sido creado')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'static/formulario.html', context)

def index(request):
    return HttpResponse('Hola mundo')