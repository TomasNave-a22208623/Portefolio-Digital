# Generated by Django 4.0.6 on 2024-05-17 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogue', '0011_alter_comentario_artigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogue.autor'),
        ),
    ]
