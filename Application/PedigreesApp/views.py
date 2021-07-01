from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_pedigrees(request):
    return HttpResponse('Hello World')