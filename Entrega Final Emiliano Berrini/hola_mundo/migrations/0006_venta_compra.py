# Generated by Django 4.1.7 on 2023-04-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hola_mundo', '0005_rename_apellidocomprador_venta_apellido_comprador_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='compra',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]