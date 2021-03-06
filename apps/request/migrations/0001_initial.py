# Generated by Django 4.0.3 on 2022-03-17 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Peticion')),
                ('body', models.TextField(verbose_name='Body de Peticion')),
                ('response', models.TextField(verbose_name='Respuesta peticion')),
                ('status_respuesta', models.IntegerField(verbose_name='Status peticion')),
                ('conversation_id', models.UUIDField(verbose_name='ID conversacion')),
                ('algoritmo', models.CharField(max_length=100)),
                ('site_id', models.CharField(max_length=10)),
                ('bot_name', models.CharField(max_length=100)),
            ],
        ),
    ]
