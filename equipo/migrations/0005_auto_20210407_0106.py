# Generated by Django 3.1.7 on 2021-04-07 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0004_auto_20210320_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='numero',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Numero de camiseta del jugador', null=True, unique=True, verbose_name='Numero'),
        ),
    ]
