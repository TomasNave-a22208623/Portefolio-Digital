# Generated by Django 4.0.6 on 2024-04-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogue', '0004_alter_classificacao_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificacao',
            name='valor',
            field=models.IntegerField(choices=[(1, '1'), (2, '1.5'), (3, '2'), (4, '2.5'), (5, '3'), (6, '3.5'), (7, '4'), (8, '4.5'), (9, '5')], default=1),
        ),
    ]
