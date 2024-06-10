from django.shortcuts import render
from django.http import HttpResponse



def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")


def liliana(request):
    return HttpResponse("Liliana a minha melhor amiga")


def sussana(request):
    return HttpResponse("Sussana a minha amiga")




