# Generated by Django 4.0.6 on 2024-05-14 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0007_remove_album_musicas_musica_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='bandas.album'),
        ),
    ]
