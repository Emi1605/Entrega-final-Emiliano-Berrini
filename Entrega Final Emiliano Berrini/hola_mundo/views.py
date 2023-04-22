from django.shortcuts import render
from django.http import HttpResponse
from hola_mundo.models import *
from hola_mundo.forms import *
from django.views.generic import ListView


def inicio(request):
    return render(request, "hola_mundo/inicio.html")

def ventas(request):
    return render(request, "hola_mundo/ventas.html")

def personas(request):
    return render(request, "hola_mundo/personas.html")

def productos(request):
    return render(request, "hola_mundo/productos.html")

def mostrar_personas(request):
    
    personas = persona.objects.all()
    return render(request, "hola_mundo/personas.html", {"personas": personas,"form":PersonaForm() })
    
def crear_personas(request):
    
    f = PersonaForm(request.POST)
    context = {
        "form": f
    }

    if f.is_valid():
        persona(nombre = f.data["nombre"], apellido = f.data["apellido"], mail = f.data["mail"], nacimiento = f.data["nacimiento"]).save()
        context["form"] = PersonaForm()
        
        context["personas"] = persona.objects.all()
        
    
    return render(request,"hola_mundo/personas.html", context)


class buscarpersonas(ListView):
    model = persona
    context_object_name = "personas"
    def get_queryset(self):
        f = BuscarPersonasForm(self.request.GET)
        if f.is_valid():
            return persona.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return persona.objects.none()
    
def mostrar_productos(request):
    
    productos = producto.objects.all()
    return render(request, "hola_mundo/productos.html", {"productos": productos,"form":ProductoForm()})

def crear_productos(request):
    
    f = ProductoForm(request.POST)
    context = {
        "form": f
    }

    if f.is_valid():
        producto(nombre_Producto = f.data["nombre_Producto"], precio_unidad = f.data["precio_unidad"], descripcion = f.data["descripcion"]).save()
        context["form"] = ProductoForm()
        
        context["productos"] = producto.objects.all()
        
    
    return render(request,"hola_mundo/productos.html", context)

class buscarProductos(ListView):
    model = producto
    context_object_name = "productos"
    def get_queryset(self):
        f = BuscarProductosForm(self.request.GET)
        if f.is_valid():
            return producto.objects.filter(nombre_Producto__icontains=f.data["Producto_nombre"]).all()
        return producto.objects.none()

def mostrar_ventas(request):
    
    ventas = venta.objects.all()
    return render(request, "hola_mundo/ventas.html", {"ventas": ventas,"form":VentaForm()})

def crear_ventas(request):
    
    f = VentaForm(request.POST)
    context = {
        "form": f
    }

    if f.is_valid():
        venta(nombre_comprador = f.data["nombre_comprador"], apellido_comprador = f.data["apellido_comprador"], numero_venta = f.data["numero_factura"], compra = f.data["compra"]).save()
        context["form"] = VentaForm()
        
        context["ventas"] = venta.objects.all()
        
    
    return render(request,"hola_mundo/ventas.html", context)

class buscarVentas(ListView):
    model = venta
    context_object_name = "ventas"
    def get_queryset(self):
        f = BuscarVentaForm(self.request.GET)
        if f.is_valid():
            return venta.objects.filter(numero_venta__icontains=f.data["Venta_id"]).all()
        return venta.objects.none()