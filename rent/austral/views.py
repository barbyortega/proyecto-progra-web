from django.shortcuts import render
from django.http import HttpResponse
from .models import Auto

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
    request.session["usuraio"]="barby"
    usuario=request.session["ususario"]
    context={'usuario':usuario}
    return render(request, 'html/admin.html', context)

def admin(request):
    Auto=Auto.objects.all()
    context={'auto':Auto}
    return render(request,'html/vehiculo.html',context)

def agregar(request):
    if request.method is not "POST":
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

def encontrar(request,pk):
    if pk != " ":
        Auto=Auto.objects.get(id_auto=pk)
        Marca=Marca.objects.all()
        print(type(Marca.id_auto.auto))
    context={'Auto':Auto,'Marca':Marca}
    if Auto:
        return render(request,'html/modificar.html',context)
    else:
        context={'mensaje':'Error, id auto no existe'}
        return render(request,'html/admin.html',context)
    
def modificar(request):

    if request.method=="POST":
        idauto=request.POST["idauto"]
        nombre=request.POST["nombre"]
        annio=request.POST["fecha"]
        Marca=request.POST["Marca"]
        color=request.POST["color"]
        cant_pasajeros=request.POST["cant_pasajeros"]
        activo="1"
    
        objauto=Auto.objects.get(id_auto = Auto)

        Auto=Auto()
        Auto.id_auto=idauto
        Auto.nombre=nombre
        Auto.annio=annio
        Auto.Marca=Marca
        Auto.color=color
        Auto.cant_pasajeros=cant_pasajeros
        Auto.activo=1
        Auto.save()
        Auto=Auto.objects.all()
        context={'mensaje':'OK, datos actualizados con éxito','nombre':Auto,'marca':Auto}
        return render(request,'html/modificar.html',context)
    else:
        Auto=Auto.objects.all()
        context={'auto':Auto}
        return render(request,'html/admin.html',context)
    
def eliminar(request,pk):
    context={}
    try:
        Auto=Auto.objects.get(id_auto=pk)
        Auto.delete()
        mensaje="Ok, Datos eliminados satisfactoriamente"
        Auto=Auto.objects.all()
        context={'auto':Auto,'mensaje':mensaje}
        return render(request,'html/admin.html',context)
    except:
        mensaje="Error, id auto no existe"
        Auto=Auto.objects.all()
        context={'auto':Auto,'mensaje':mensaje}
        return render(request,'html/admin.html',context)
