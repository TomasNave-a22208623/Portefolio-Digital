from django.shortcuts import render, get_object_or_404
from .models import Festival, Localizacao

def lista_festivais(request):
    localizacoes = Localizacao.objects.all()
    return render(request, 'festivais/pagina_listafestivais.html', {'localizacoes': localizacoes})

def festival(request, festival_id):
    festival = get_object_or_404(Festival, pk=festival_id)
    return render(request, 'festivais/pagina_festival.html', {'festival': festival})





