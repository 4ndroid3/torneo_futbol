# Generated by Django 3.1.7 on 2021-03-18 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0002_auto_20210317_2330'),
        ('campeonato', '0002_auto_20210318_0109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clasificacion',
            options={'verbose_name': 'Clasificación', 'verbose_name_plural': 'Clasificaciones'},
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='derrotas',
            field=models.PositiveIntegerField(default=0, help_text='Derrotas del equipo en el campeonato', verbose_name='Derrotas'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='empates',
            field=models.PositiveIntegerField(default=0, help_text='Empates del equipo en el campeonato', verbose_name='Empates'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='goles_contra',
            field=models.PositiveIntegerField(default=0, help_text='Goles que le convirtieron al equipo en el campeonato', verbose_name='Goles en contra'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='goles_favor',
            field=models.PositiveIntegerField(default=0, help_text='Goles convertidos por el equipo en el campeonato', verbose_name='Goles a favor'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='id_campeonato',
            field=models.ForeignKey(default=0, help_text='Nombre del Campeonato', on_delete=django.db.models.deletion.CASCADE, to='campeonato.campeonato', verbose_name='Campeonato'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='id_equipo',
            field=models.ForeignKey(default=0, help_text='Nombre del equipo', on_delete=django.db.models.deletion.CASCADE, to='equipo.equipo', verbose_name='Equipo'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='partidos_jugados',
            field=models.PositiveIntegerField(default=0, help_text='Partidos jugados por el equipo en el campeonato', verbose_name='Partidos Jugados'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='puntos',
            field=models.IntegerField(default=0, help_text='Puntos acumulados por equipo', verbose_name='Puntos'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='victorias',
            field=models.PositiveIntegerField(default=0, help_text='Victorias del equipo en el campeonato', verbose_name='Victorias'),
        ),
    ]