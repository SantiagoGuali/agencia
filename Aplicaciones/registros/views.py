from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ciudad, Propietario, Modelo, Vehiculo
from django.contrib import messages

# Vista para listar ciudades

def inicio(request):
    return render(request, 'home.html')

def ciudad(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'ciudad.html', {'ciudades': ciudades})

# Vista para agregar ciudad
def agregarCiudad(request):
    if request.method == 'POST':
        nombre_city = request.POST.get('nombre_city')
        ciudad = Ciudad(nombre_city=nombre_city)
        ciudad.save()
        messages.success(request, "La ciudad ha sido registrada exitosamente.")
        return redirect('ciudad')
    return render(request, 'ciudad.html')

# Vista para eliminar ciudad
def eliminarCiudad(request, id_ciudad):
    ciudad = get_object_or_404(Ciudad, id=id_ciudad)
    ciudad.delete()
    messages.success(request, "Ciudad eliminada exitosamente.")
    return redirect('ciudad')

# Vista para editar ciudad
def editarCiudad(request, id_ciudad):
    ciudad = get_object_or_404(Ciudad, id=id_ciudad)
    if request.method == 'POST':
        ciudad.nombre_city = request.POST.get('nombre_city')
        ciudad.save()
        messages.success(request, "Ciudad actualizada exitosamente.")
        return redirect('ciudad')
    return render(request, 'editar_ciudad.html', {'ciudad': ciudad})


# Vista para listar modelos
def modelo(request):
    modelos = Modelo.objects.all()
    return render(request, 'modelo.html', {'modelos': modelos})

# Vista para agregar modelo
def agregarModelo(request):
    if request.method == 'POST':
        nombre_mod = request.POST.get('nombre_mod')
        modelo = Modelo(nombre_mod=nombre_mod)
        modelo.save()
        messages.success(request, "Modelo registrado exitosamente.")
        return redirect('modelo')
    return render(request, 'modelo.html')

# Vista para eliminar modelo
def eliminarModelo(request, id_modelo):
    modelo = get_object_or_404(Modelo, id=id_modelo)
    modelo.delete()
    messages.success(request, "Modelo eliminado exitosamente.")
    return redirect('modelo')

# Vista para editar modelo
def editarModelo(request, id_modelo):
    modelo = get_object_or_404(Modelo, id=id_modelo)
    if request.method == 'POST':
        modelo.nombre_mod = request.POST.get('nombre_mod')
        modelo.estado_mod = request.POST.get('estado_mod') == 'on'
        modelo.save()
        messages.success(request, "Modelo actualizado exitosamente.")
        return redirect('modelo')
    return render(request, 'editar_modelo.html', {'modelo': modelo})





# Vista para listar propietarios
def propietario(request):
    propietarios = Propietario.objects.all()
    return render(request, 'propietario.html', {'propietarios': propietarios})

def obtener_ciudades(request):
    ciudades = Ciudad.objects.all()
    data = list(ciudades.values('id', 'nombre_city'))
    return JsonResponse(data, safe=False)

# Vista para agregar propietario
def agregarPropietario(request):
    if request.method == 'POST':
        nombre_prop = request.POST.get('nombre_prop')
        apellido_prop = request.POST.get('apellido_prop')
        email_prop = request.POST.get('email_prop')
        telefono_prop = request.POST.get('telefono_prop')
        fk_id_city = request.POST.get('fk_id_city')
        ciudad = Ciudad.objects.get(id=fk_id_city)
        
        propietario = Propietario(
            nombre_prop=nombre_prop,
            apellido_prop=apellido_prop,
            email_prop=email_prop,
            telefono_prop=telefono_prop,
            fk_id_city=ciudad
        )
        propietario.save()
        messages.success(request, "Propietario registrado exitosamente.")
        return redirect('propietario')
    ciudades = Ciudad.objects.all()
    return render(request, 'agregar_propietario.html', {'ciudades': ciudades})

# Vista para eliminar propietario
def eliminarPropietario(request, id_propietario):
    propietario = get_object_or_404(Propietario, id=id_propietario)
    propietario.delete()
    messages.success(request, "Propietario eliminado exitosamente.")
    return redirect('propietario')

# Vista para editar propietario
def editarPropietario(request, id_propietario):
    propietario = get_object_or_404(Propietario, id=id_propietario)
    if request.method == 'POST':
        propietario.nombre_prop = request.POST.get('nombre_prop')
        propietario.apellido_prop = request.POST.get('apellido_prop')
        propietario.email_prop = request.POST.get('email_prop')
        propietario.telefono_prop = request.POST.get('telefono_prop')
        propietario.fk_id_city = Ciudad.objects.get(id=request.POST.get('fk_id_city'))
        propietario.save()
        messages.success(request, "Propietario actualizado exitosamente.")
        return redirect('propietario')
    
    ciudades = Ciudad.objects.all()
    return render(request, 'editar_propietario.html', {'propietario': propietario, 'ciudades': ciudades})


# Vista para listar vehículos
def vehiculo(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo.html', {'vehiculos': vehiculos})

# Vista para agregar vehículo
def agregarVehiculo(request):
    if request.method == 'POST':
        fk_id_mod = request.POST.get('fk_id_mod')
        fabricacion_veh = request.POST.get('fabricacion_veh')
        precio_veh = request.POST.get('precio_veh')
        color_veh = request.POST.get('color_veh')
        placa_veh = request.POST.get('placa_veh')
        
        modelo = Modelo.objects.get(id=fk_id_mod)
        
        vehiculo = Vehiculo(
            fk_id_mod=modelo,
            fabricacion_veh=fabricacion_veh,
            precio_veh=precio_veh,
            color_veh=color_veh,
            placa_veh=placa_veh
        )
        vehiculo.save()
        messages.success(request, "Vehículo registrado exitosamente.")
        return redirect('vehiculo')
    
    modelos = Modelo.objects.all()
    return render(request, 'agregar_vehiculo.html', {'modelos': modelos})

# Vista para eliminar vehículo
def eliminarVehiculo(request, id_vehiculo):
    vehiculo = get_object_or_404(Vehiculo, id=id_vehiculo)
    vehiculo.delete()
    messages.success(request, "Vehículo eliminado exitosamente.")
    return redirect('vehiculo')

# Vista para editar vehículo
def editarVehiculo(request, id_vehiculo):
    vehiculo = get_object_or_404(Vehiculo, id=id_vehiculo)
    if request.method == 'POST':
        vehiculo.fk_id_mod = Modelo.objects.get(id=request.POST.get('fk_id_mod'))
        vehiculo.fabricacion_veh = request.POST.get('fabricacion_veh')
        vehiculo.precio_veh = request.POST.get('precio_veh')
        vehiculo.color_veh = request.POST.get('color_veh')
        vehiculo.placa_veh = request.POST.get('placa_veh')
        vehiculo.save()
        messages.success(request, "Vehículo actualizado exitosamente.")
        return redirect('vehiculo')

    modelos = Modelo.objects.all()
    return render(request, 'editar_vehiculo.html', {'vehiculo': vehiculo, 'modelos': modelos})

# Vista para mostrar los vehículos y los select de los modelos, propietarios y ciudades
def vehiculos_view(request):
    ciudades = Ciudad.objects.all()  # Obtener todas las ciudades
    propietarios = Propietario.objects.all()  # Obtener todos los propietarios
    modelos = Modelo.objects.all()  # Obtener todos los modelos de vehículos

    # Pasar los datos a la plantilla
    return render(request, 'vehiculos.html', {
        'ciudades': ciudades,
        'propietarios': propietarios,
        'modelos': modelos
    })
