from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    mail = forms.CharField(max_length=100)
    nacimiento = forms.DateField()

class BuscarPersonasForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=100)

class ProductoForm(forms.Form):
    nombre_Producto =  forms.CharField(max_length=100)
    precio_unidad = forms.IntegerField()
    descripcion = forms.CharField(max_length=100)


class BuscarProductosForm(forms.Form):
    Producto_nombre = forms.CharField(max_length=100)

class VentaForm(forms.Form):
    nombre_comprador = forms.CharField(max_length=100)
    apellido_comprador = forms.CharField(max_length=100)
    numero_factura = forms.IntegerField()
    compra = forms.CharField(max_length=100)

class BuscarVentaForm(forms.Form):
    Venta_id = forms.IntegerField()