from django.urls import path
from appcoder.views import *


urlpatterns = [
    path ("inicio/", home),
    path ("modelos/", modelos),
    path ("marcas/", marcas),
    path ("peticiones ventas/", peticiones_ventas),
    path ("seccion ingreso/", seccion_ingreso),
]





