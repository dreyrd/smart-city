# Generated by Django 5.1.1 on 2024-09-26 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_address', models.CharField(max_length=20, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('localizacao', models.CharField(max_length=100)),
                ('responsavel', models.CharField(max_length=100)),
                ('unidade_medida', models.CharField(blank=True, max_length=20, null=True)),
                ('status_operacional', models.BooleanField(default=True)),
                ('observacao', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipos_sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='usuario',
        ),
        migrations.AddField(
            model_name='sensor',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_smart.tipos_sensor'),
        ),
    ]
