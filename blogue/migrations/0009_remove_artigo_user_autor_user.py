# Generated by Django 4.0.6 on 2024-05-17 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogue', '0008_alter_artigo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artigo',
            name='user',
        ),
        migrations.AddField(
            model_name='autor',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
