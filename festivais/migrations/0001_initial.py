# Generated by Django 4.0.6 on 2024-04-24 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagensFestivais/')),
                ('link', models.URLField(blank=True, null=True)),
                ('bandas', models.ManyToManyField(to='festivais.banda')),
                ('localizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festivais.localizacao')),
            ],
        ),
    ]
