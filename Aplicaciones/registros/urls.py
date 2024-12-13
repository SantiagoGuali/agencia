from django.urls import path
from .import views
urlpatterns = [
    path('', views.inicio),
    path('ciudades', views.ciudad, name='ciudad'),
    path('agregar_ciudad/', views.agregarCiudad, name='agregarCiudad'),
    path('eliminar_ciudad/<int:id_ciudad>/', views.eliminarCiudad, name='eliminarCiudad'),
    path('editar_ciudad/<int:id_ciudad>/', views.editarCiudad, name='editarCiudad'),

    path('propietarios/', views.propietario, name='propietario'),
    path('agregar_propietario/', views.agregarPropietario, name='agregarPropietario'),
    path('eliminar_propietario/<int:id_propietario>/', views.eliminarPropietario, name='eliminarPropietario'),
    path('editar_propietario/<int:id_propietario>/', views.editarPropietario, name='editarPropietario'),

    path('modelos/', views.modelo, name='modelo'),
    path('agregar_modelo/', views.agregarModelo, name='agregarModelo'),
    path('eliminar_modelo/<int:id_modelo>/', views.eliminarModelo, name='eliminarModelo'),
    path('editar_modelo/<int:id_modelo>/', views.editarModelo, name='editarModelo'),
    path('obtener_ciudades/', views.obtener_ciudades, name='obtener_ciudades'),

    path('vehiculos/', views.vehiculo, name='vehiculo'),
    path('agregar_vehiculo/', views.agregarVehiculo, name='agregarVehiculo'),
    path('eliminar_vehiculo/<int:id_vehiculo>/', views.eliminarVehiculo, name='eliminarVehiculo'),
    path('editar_vehiculo/<int:id_vehiculo>/', views.editarVehiculo, name='editarVehiculo'),
    path('vehiculos/', views.vehiculos_view, name='vehiculos_view'),
    
]
