from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Auto, Marca

def index(request):
    context = {
        'title': 'Austral Rent a Car - Inicio',
    }
    return render(request, 'index.html', context)

def admin2(request):
    context = {
        'title': 'Austral Rent a Car - Administración',
    }
    return render(request, 'html/admin.html', context)

def vehiculos(request):
    context = {
        'title': 'Austral Rent a Car - Vehículos',
    }
    return render(request, 'vehiculos.html', context)

def nosotros(request):
    context = {
        'title': 'Austral Rent a Car - Nosotros',
    }
    return render(request, 'equipo.html', context)

def login(request):
    contexto = {}
    return render(request,'login.html',contexto);

def menu(request):
    request.session["usuaio"]="barby"
    usuario=request.session["usuario"]
    context={'usuario':usuario}
    return render(request, 'html/admin.html', context)

def admin(request):
    Auto=Auto.objects.all()
    context={'auto':Auto}
    return render(request,'html/vehiculo.html',context)

def agregar(request):
    if request.method !="POST":
        Auto=Auto.objects.all();
        context={'idauto':Auto}
        return render(request,'html/agregar.html',context)
    else:
        #Es un POST,por lo tanto se recuperan los datos del formulario
        id_auto =request.POST["idAuto"]
        nombre=request.POST["nombre"]
        annio=request.POST["fecha"]
        Marca=request.POST["Marca"]
        activo="1"
    
    
        obj=Auto.objects.create(id_auto=id_auto,
                                   nombre=nombre,
                                   annio=annio,
                                   Marca=Marca,
                                   activo=1)
        obj.save()
        context={'mensaje':'OK, datos guardados con éxito'}
        return render(request,'html/agregar.html',context)

def encontrar(request, pk):
    context = {}
    try:
        auto = Auto.objects.get(id_auto=pk)
        marcas = Marca.objects.all()  
        context = {'auto': auto, 'marcas': marcas}
        return render(request, 'html/modificar.html', context)
    except Auto.DoesNotExist:
        context = {'mensaje': 'Error, id auto no existe'}
        return render(request, 'html/admin.html', context)

def modificar(request):
    if request.method == "POST":
        idauto = request.POST["idauto"]
        nombre = request.POST["nombre"]
        annio = request.POST["fecha"]
        marca = request.POST["marca"]  # Suponiendo que "marca" es el nombre correcto del campo
        color = request.POST["color"]
        cant_pasajeros = request.POST["cant_pasajeros"]
        activo = "1"

        try:
            auto = Auto.objects.get(id_auto=idauto)
            auto.nombre = nombre
            auto.annio = annio
            auto.marca = marca  # Asegúrate de que el nombre del campo sea correcto según tu modelo
            auto.color = color
            auto.cant_pasajeros = cant_pasajeros
            auto.activo = activo
            auto.save()
            autos = Auto.objects.all()
            context = {'mensaje': 'OK, datos actualizados con éxito', 'autos': autos}
            return render(request, 'html/modificar.html', context)
        except Auto.DoesNotExist:
            autos = Auto.objects.all()
            context = {'autos': autos, 'mensaje': 'Error, auto no encontrado'}
            return render(request, 'html/admin.html', context)
    else:
        autos = Auto.objects.all()
        context = {'autos': autos}
        return render(request, 'html/admin.html', context)


def eliminar(request, pk):
    try:
        auto = Auto.objects.get(id_auto=pk)
        auto.delete()
        mensaje = "Ok, Datos eliminados satisfactoriamente"
    except Auto.DoesNotExist:
        mensaje = "Error, id auto no existe"

    autos = Auto.objects.all()
    context = {'autos': autos, 'mensaje': mensaje}
    return render(request, 'html/admin.html', context)

