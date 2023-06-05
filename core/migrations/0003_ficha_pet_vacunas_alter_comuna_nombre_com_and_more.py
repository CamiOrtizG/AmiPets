# Generated by Django 4.0.5 on 2023-05-31 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_vacuna_f_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha_pet',
            name='vacunas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.vacuna'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comuna',
            name='nombre_com',
            field=models.CharField(max_length=60, verbose_name='Comuna'),
        ),
        migrations.AlterField(
            model_name='estadia',
            name='descrip_est',
            field=models.CharField(max_length=200, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.CharField(max_length=60, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='profesion',
            field=models.CharField(blank=True, max_length=60, verbose_name='Profesion'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombres',
            field=models.CharField(max_length=100, verbose_name='Nombre completo'),
        ),
        migrations.AlterField(
            model_name='region',
            name='nombre_r',
            field=models.CharField(max_length=100, verbose_name='Región'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='descrip',
            field=models.TextField(max_length=200, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='descrip_vac',
            field=models.CharField(max_length=100, verbose_name='Descripción vacunas'),
        ),
    ]
