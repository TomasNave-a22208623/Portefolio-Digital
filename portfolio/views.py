import requests
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def landing_page(request):

    previsaoLisboa_url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

#--------------------------------------------------(Extrair tipos de Tempo)-----------------------------------------------------------------------
    previsao_response = requests.get(previsaoLisboa_url)
    if previsao_response.status_code == 200:
        dic_previsao = previsao_response.json()
        previsao_hoje = dic_previsao['data'][0]  # Guarda o primeiro dicionário do JSON que é o do dia de hoje
    else:
        previsao_hoje = {}

#--------------------------------------------------(Extrair tipos de Tempo)---------------------------------------------------------------------------
    # {
    #     "descWeatherTypeEN":"Cloudy (High cloud)",
    #      "descWeatherTypePT":"C\u00e9u nublado por nuvens altas",
    #      "idWeatherType":5                                           ----------> w_ic_d_{idWeatherType}anim.svg
    # },                                                                serve para ir buscar a imagem



    weather_types_response = requests.get(weather_types_url)
    if weather_types_response.status_code == 200:
        weather_types_data = weather_types_response.json()
        weather_types_list = weather_types_data.get('data', [])  # Acesse a lista de tipos de tempo
        weather_types = {item['idWeatherType']: item for item in weather_types_list}  # Cria o dicionário chave: idWeather | objeto todo
    else:
        weather_types = {}

 #--------------------------------------------------(Extrair variaveis precisas)---------------------------------------------------------------------------


    city_name = "Lisboa"
    min_temp = previsao_hoje.get('tMin', 'N/A')
    max_temp = previsao_hoje.get('tMax', 'N/A')
    dataDeHoje = previsao_hoje.get('forecastDate', 'N/A')
    weather_type_id = previsao_hoje.get('idWeatherType', 'N/A')
    weather_description = weather_types.get(weather_type_id, {}).get('descWeatherTypePT', 'N/A')

#--------------------------------------------------(Procurar foto relativa ao tempo)---------------------------------------------------------------------------

    icon_filename = f"w_ic_d_{weather_type_id:02d}anim.svg"
    icon_url = f"/static/meteo/{icon_filename}"

#---------------------------------------------------------------------------------------------------------------------------------------------
    context = {
        'cidade': city_name,
        'min_temp': min_temp,
        'max_temp': max_temp,
        'dataDeHoje': dataDeHoje,
        'descricaoTempo': weather_description,
        'icon_url': icon_url,
    }






    return render(request, 'portfolio/landing_page.html', context)

def contactos(request):
    return render(request, 'portfolio/contactos.html')


def sobre_view(request):
    return render(request, 'portfolio/sobre.html')

def programacao_view(request):
    return render(request, 'portfolio/programacao.html')
