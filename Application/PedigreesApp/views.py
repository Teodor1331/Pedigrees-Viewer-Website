from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

from . import list_families

def view_pedigrees(request, *args, **kwargs):
    list_pedigrees = []
    list_file_names = []

    for i in range(0, len(list_families)):
        list_pedigrees.append(list_families[i].identifier)
        list_file_names.append(str(list_pedigrees[len(list_pedigrees) - 1]) + ".html")

        list_pedigrees.sort()
        list_file_names.sort()

    dictionary = {
        "pedigrees": list_pedigrees,
        "file_names": list_file_names
    }

    return render(request, "view_pedigrees.html", dictionary)

def view_pedigrees_new(request, pedigree_name):
    return render(request, pedigree_name)