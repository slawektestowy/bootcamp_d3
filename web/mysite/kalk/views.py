from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def add_numbers(request, l1, l2):
    return HttpResponse(content=f'{l1 + l2}')