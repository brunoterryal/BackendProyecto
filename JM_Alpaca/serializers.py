from rest_framework import serializers
from JM_Alpaca.models import Boleta,Compra,Producto,Proveedor,TipoDescuento,TipoFactor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proveedor
        fields=('IdProveedor','NombreProveedor','ApellidosProveedor','SedeProveedor','EstadoProveedor')

class TipoDescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoDescuento
        fields=('IdTipoDescuento','NombreTipoDescuento','EstadoTipoDescuento')

class TipoFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoFactor
        fields=('IdTipoFactor','NombreTipoFactor','EstadoTipoFactor')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields=('IdProducto','ProveedorProducto','TipoDescuentoProducto','CantidadProducto','MontoProducto','DescuentoProducto')

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Compra
        fields=('IdCompra','ProveedorCompra','TipoFactorCompra','FactorCompra','FechaCompra')

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Boleta
        fields=('IdBoleta','FechaBoleta','ProductoBoleta','PesoProducto','TotalBoleta')
        