from django.conf.urls import url
from JM_Alpaca import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^boleta$',views.boletaApi),
    url(r'^boleta/([0-9]+)$',views.boletaApi),
    
    url(r'^compra$',views.compraApi),
    url(r'^compra/([0-9]+)$',views.compraApi),

    url(r'^producto$',views.productoApi),
    url(r'^producto/([0-9]+)$',views.productoApi),

    url(r'^proveedor$',views.proveedorApi),
    url(r'^proveedor/([0-9]+)$',views.proveedorApi),

    url(r'^tipoDescuento$',views.tipoDescuentoApi),
    url(r'^tipoDescuento/([0-9]+)$',views.tipoDescuentoApi),

    url(r'^tipoFactor$',views.tipoFactorApi),
    url(r'^tipoFactor/([0-9]+)$',views.tipoFactorApi),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)