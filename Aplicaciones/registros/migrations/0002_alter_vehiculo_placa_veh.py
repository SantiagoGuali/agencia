# Generated by Django 5.1.4 on 2024-12-13 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='placa_veh',
            field=models.CharField(max_length=20),
        ),
    ]