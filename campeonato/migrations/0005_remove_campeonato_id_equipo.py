# Generated by Django 3.1.7 on 2021-03-22 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campeonato', '0004_auto_20210320_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campeonato',
            name='id_equipo',
        ),
    ]
