# pwsite/views.py

from django.shortcuts import render

def index_view(request):
    return render(request, "novaapp/index.html")
    
    
def heroes_view(request):
    return render(request, "novaapp/herois_dc.html")
    
def viloes_view(request):
    return render(request, "novaapp/viloes_dc.html")
