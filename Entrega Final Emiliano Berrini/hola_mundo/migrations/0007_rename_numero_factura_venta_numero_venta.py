# Generated by Django 4.1.7 on 2023-04-21 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hola_mundo', '0006_venta_compra'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='numero_factura',
            new_name='numero_venta',
        ),
    ]
