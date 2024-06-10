from bandas.models import *
import json

Banda.objects.all().delete()
Album.objects.all().delete()
Musica.objects.all().delete()

def importar_bandas():


    with open ('bandas/json/bandas.json') as f:
        bandas = json.load(f)

        for banda , info in bandas.items():
            print(banda,info['genero'],info['foto'],info['nacionalidade'],info['anoDeCriacao'])

            Banda.objects.create(
                nome = banda,
                genero = info['genero'],
                foto = info['foto'],
                nacionalidade = info['nacionalidade'],
                anoDeCriacao = info['anoDeCriacao']
            )


    with open('bandas/json/Albuns.json') as f:
        albuns_data = json.load(f)
        for album_data in albuns_data:
            banda = Banda.objects.get(nome=album_data['banda'])
            album = Album.objects.create(
                titulo=album_data['titulo'],
                ano=album_data['ano'],
                capa=album_data['capa'],
                banda=banda
            )

            for musica_data in album_data['musicas']:
                musica = Musica.objects.create(
                    titulo=musica_data['titulo'],
                    duracao=musica_data['duracao'],
                    spotify_link=musica_data['spotify_link'],
                    album=album
                )


    print("Importação concluida")







