from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def turma(request):
    pagina='bye'
    return HttpResponse(pagina)