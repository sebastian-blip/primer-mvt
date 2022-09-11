import json

from .models import Family
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib import messages


def ver_familia(request):
    familia = Family.objects.all()
    datos = {'list_familia': familia}
    final = render(request, 'familia.html', datos)
    return HttpResponse(final)


def post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Family.objects.create(
                nombre=form.cleaned_data['nombre'],
                parentesco=form.cleaned_data['parentesco'],
                edad=form.cleaned_data['edad'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento']
            )
            messages.success(request, 'Familiar guardado')
            return redirect('mi_familia:ver_familiar')

    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})






