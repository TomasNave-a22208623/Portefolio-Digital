# Generated by Django 4.0.6 on 2024-04-06 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0005_alter_banda_anodecriacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='banda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albuns', to='bandas.banda'),
        ),
        migrations.AlterField(
            model_name='banda',
            name='genero',
            field=models.CharField(max_length=200),
        ),
    ]
