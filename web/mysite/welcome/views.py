from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_view(request):
    return HttpResponse(content="Czesc Witaj Swiecie")

def hello_name_view(request, name):
    return HttpResponse(content=f'Czesc {name}! Jak sie masz? :)')
