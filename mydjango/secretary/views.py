from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Je suis dans le secretariat!")

    # vas dans le dossier mydjango et regarde comment j'appelle le template
