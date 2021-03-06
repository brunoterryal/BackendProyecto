# Generated by Django 3.2.8 on 2021-10-16 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('IdProveedor', models.AutoField(primary_key=True, serialize=False)),
                ('NombreProveedor', models.CharField(max_length=250)),
                ('ApellidosProveedor', models.CharField(max_length=250)),
                ('SedeProveedor', models.CharField(max_length=250)),
                ('EstadoProveedor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoDescuento',
            fields=[
                ('IdTipoDescuento', models.AutoField(primary_key=True, serialize=False)),
                ('NombreTipoDescuento', models.CharField(max_length=50)),
                ('EstadoTipoDescuento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoFactor',
            fields=[
                ('IdTipoFactor', models.AutoField(primary_key=True, serialize=False)),
                ('NombreTipoFactor', models.CharField(max_length=50)),
                ('EstadoTipoFactor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('IdProducto', models.AutoField(primary_key=True, serialize=False)),
                ('CantidadProducto', models.IntegerField()),
                ('MontoProducto', models.IntegerField()),
                ('DescuentoProducto', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ProveedorProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JM_Alpaca.proveedor')),
                ('TipoDescuentoProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JM_Alpaca.tipodescuento')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('IdCompra', models.AutoField(primary_key=True, serialize=False)),
                ('FactorCompra', models.IntegerField()),
                ('FechaCompra', models.DateField()),
                ('ProveedorCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JM_Alpaca.proveedor')),
                ('TipoFactorCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JM_Alpaca.tipofactor')),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('IdBoleta', models.AutoField(primary_key=True, serialize=False)),
                ('FechaBoleta', models.DateField()),
                ('PesoProducto', models.IntegerField()),
                ('TotalBoleta', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ProductoBoleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JM_Alpaca.producto')),
            ],
        ),
    ]
