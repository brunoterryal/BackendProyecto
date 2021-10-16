from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# Create your views here.

from JM_Alpaca.models import Boleta,Compra,Producto,Proveedor,TipoDescuento,TipoFactor
from JM_Alpaca.serializers import BoletaSerializer,CompraSerializer,ProductoSerializer,ProveedorSerializer,TipoDescuentoSerializer,TipoFactorSerializer

#BOLETA
@csrf_exempt
def boletaApi(request,id=0):
    if request.method=='GET':
        boletas = Boleta.objects.all()
        boletas_serializer=BoletaSerializer(boletas,many=True)
        return JsonResponse(boletas_serializer.data,safe=False)
    elif request.method=='POST':
        boleta_data=JSONParser().parse(request)
        boletas_serializer=BoletaSerializer(data=boleta_data)
        if boletas_serializer.is_valid():
            boletas_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        boleta_data=JSONParser().parse(request)
        boleta=Boleta.objects.get(IdBoleta=boleta_data['IdBoleta'])
        boletas_serializer=BoletaSerializer(boleta,data=boleta_data)
        if boletas_serializer.is_valid():
            boletas_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        boleta=Boleta.objects.get(IdBoleta=id)
        boleta.delete()
        return JsonResponse("Deleted Successfully",safe=False)

#COMPRA
@csrf_exempt
def compraApi(request,id=0):
    if request.method=='GET':
        compras = Compra.objects.all()
        compras_serializer=CompraSerializer(compras,many=True)
        return JsonResponse(compras_serializer.data,safe=False)
    elif request.method=='POST':
        compra_data=JSONParser().parse(request)
        compras_serializer=CompraSerializer(data=compra_data)
        if compras_serializer.is_valid():
            compras_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        compra_data=JSONParser().parse(request)
        compra=Compra.objects.get(IdCompra=compra_data['IdCompra'])
        compras_serializer=CompraSerializer(compra,data=compra_data)
        if compras_serializer.is_valid():
            compras_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        compra=Compra.objects.get(IdCompra=id)
        compra.delete()
        return JsonResponse("Deleted Successfully",safe=False)

#PRODUCTO
@csrf_exempt
def productoApi(request,id=0):
    if request.method=='GET':
        productos = Producto.objects.all()
        productos_serializer=ProductoSerializer(productos,many=True)
        return JsonResponse(productos_serializer.data,safe=False)
    elif request.method=='POST':
        producto_data=JSONParser().parse(request)
        productos_serializer=ProductoSerializer(data=producto_data)
        if productos_serializer.is_valid():
            productos_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        producto_data=JSONParser().parse(request)
        producto=Producto.objects.get(IdProducto=producto_data['IdProducto'])
        productos_serializer=ProductoSerializer(producto,data=producto_data)
        if productos_serializer.is_valid():
            productos_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        producto=Producto.objects.get(IdProducto=id)
        producto.delete()
        return JsonResponse("Deleted Successfully",safe=False)

#PROVEEDOR
@csrf_exempt
def proveedorApi(request,id=0):
    if request.method=='GET':
        proveedors = Proveedor.objects.all()
        proveedors_serializer=ProveedorSerializer(proveedors,many=True)
        return JsonResponse(proveedors_serializer.data,safe=False)
    elif request.method=='POST':
        proveedor_data=JSONParser().parse(request)
        proveedors_serializer=ProveedorSerializer(data=proveedor_data)
        if proveedors_serializer.is_valid():
            proveedors_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        proveedor_data=JSONParser().parse(request)
        proveedor=Proveedor.objects.get(IdProveedor=proveedor_data['IdProveedor'])
        proveedors_serializer=ProveedorSerializer(proveedor,data=proveedor_data)
        if proveedors_serializer.is_valid():
            proveedors_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        proveedor=Proveedor.objects.get(IdProveedor=id)
        proveedor.delete()
        return JsonResponse("Deleted Successfully",safe=False)

#TIPO_DESCUENTO
@csrf_exempt
def tipoDescuentoApi(request,id=0):
    if request.method=='GET':
        TipoDescuentos = TipoDescuento.objects.all()
        TipoDescuentos_serializer=TipoDescuentoSerializer(TipoDescuentos,many=True)
        return JsonResponse(TipoDescuentos_serializer.data,safe=False)
    elif request.method=='POST':
        TipoDescuento_data=JSONParser().parse(request)
        TipoDescuentos_serializer=TipoDescuentoSerializer(data=TipoDescuento_data)
        if TipoDescuentos_serializer.is_valid():
            TipoDescuentos_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        TipoDescuento_data=JSONParser().parse(request)
        tipoDescuento=TipoDescuento.objects.get(IdTipoDescuento=TipoDescuento_data['IdTipoDescuento'])
        TipoDescuentos_serializer=TipoDescuentoSerializer(tipoDescuento,data=TipoDescuento_data)
        if TipoDescuentos_serializer.is_valid():
            TipoDescuentos_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        tipoDescuento=TipoDescuento.objects.get(IdTipoDescuento=id)
        TipoDescuento.delete()
        return JsonResponse("Deleted Successfully",safe=False)

#TIPO_FACTOR
@csrf_exempt
def tipoFactorApi(request,id=0):
    if request.method=='GET':
        TipoFactors = TipoFactor.objects.all()
        TipoFactors_serializer=TipoFactorSerializer(TipoFactors,many=True)
        return JsonResponse(TipoFactors_serializer.data,safe=False)
    elif request.method=='POST':
        TipoFactor_data=JSONParser().parse(request)
        TipoFactors_serializer=TipoFactorSerializer(data=TipoFactor_data)
        if TipoFactors_serializer.is_valid():
            TipoFactors_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        TipoFactor_data=JSONParser().parse(request)
        tipoFactor=TipoFactor.objects.get(IdTipoFactor=TipoFactor_data['IdTipoFactor'])
        TipoFactors_serializer=TipoFactorSerializer(tipoFactor,data=TipoFactor_data)
        if TipoFactors_serializer.is_valid():
            TipoFactors_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        tipoFactor=TipoFactor.objects.get(IdTipoFactor=id)
        TipoFactor.delete()
        return JsonResponse("Deleted Successfully",safe=False)