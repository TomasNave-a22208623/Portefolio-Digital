# Generated by Django 4.0.6 on 2024-05-21 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0009_banda_biografia'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='letra',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
