from django.db import models

# Create your models here.

class Proveedor(models.Model):
    IdProveedor = models.AutoField(primary_key=True)
    NombreProveedor = models.CharField(max_length=250)
    ApellidosProveedor = models.CharField(max_length=250)
    SedeProveedor = models.CharField(max_length=250)
    EstadoProveedor = models.IntegerField()

class TipoDescuento(models.Model):
    IdTipoDescuento = models.AutoField(primary_key=True)
    NombreTipoDescuento = models.CharField(max_length=50)
    EstadoTipoDescuento = models.IntegerField()

class TipoFactor(models.Model):
    IdTipoFactor = models.AutoField(primary_key=True)
    NombreTipoFactor = models.CharField(max_length=50)
    EstadoTipoFactor = models.IntegerField()

class Producto(models.Model):
    IdProducto = models.AutoField(primary_key=True)
    ProveedorProducto = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    TipoDescuentoProducto = models.ForeignKey(TipoDescuento, on_delete=models.CASCADE)
    CantidadProducto = models.IntegerField()
    MontoProducto = models.IntegerField()
    DescuentoProducto = models.DecimalField(max_digits=4,decimal_places=2)

class Compra(models.Model):
    IdCompra = models.AutoField(primary_key=True)
    ProveedorCompra = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    TipoFactorCompra = models.ForeignKey(TipoFactor, on_delete=models.CASCADE)
    FactorCompra = models.IntegerField()
    FechaCompra = models.DateField()

class Boleta(models.Model):
    IdBoleta = models.AutoField(primary_key=True)
    FechaBoleta = models.DateField()
    ProductoBoleta = models.ForeignKey(Producto, on_delete=models.CASCADE)
    PesoProducto = models.IntegerField()
    TotalBoleta = models.DecimalField(max_digits=4,decimal_places=2)


