from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def alumni(request):
    return HttpResponse("Eu não sei o que é pior...")
def atividades(request):
    return HttpResponse("...ou a ressaca na lucidez.")
def turma(request):    
    return
def utilitarios(request):
    return
def index(request):
    return render(request, "index.html")