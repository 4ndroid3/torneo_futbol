# Generated by Django 3.1.7 on 2021-03-20 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0002_auto_20210317_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='id_equipo',
            field=models.ForeignKey(default=0, help_text='Nombre del equipo', on_delete=django.db.models.deletion.CASCADE, to='equipo.equipo', verbose_name='Equipo'),
        ),
    ]
