from django.shortcuts import render
from django.http import HttpResponse
from models import Pages


# Create your views here.

def handler(request, recurso):
    fila = Pages.objects.filter(name=recurso)
    if len(fila) == 0:
        if recurso == "":
            fila = Pages(name=recurso, page="Pagina principal")
        else:
            fila = Pages(name=recurso, page="Pagina de " + recurso)
        fila.save()
        return HttpResponse(fila.page)
    else:
        return HttpResponse(fila[0].page)
