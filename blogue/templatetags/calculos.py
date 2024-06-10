from django import template

register = template.Library()

@register.filter
def calcular_media_classificacoes(classificacoes):
    if classificacoes:
        total = 0
        count = 0
        for classificacao in classificacoes:
            total += classificacao.valor
            count += 1
        media = total / count
        return round(media, 1)
    else:
        return None