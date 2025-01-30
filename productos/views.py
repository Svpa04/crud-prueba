from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm



# Create your views here.
def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listado_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        costo = request.POST['costo']
        producto = Producto(nombre=nombre, precio=precio, descripcion=descripcion, costo=costo)
        producto.save()
        return redirect('listado_productos')
    return render(request, 'productos/crear_producto.html')

def editar_producto(request, id):
    productos = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=productos)
        if form.is_valid():
            form.save()
            return redirect('listado_productos')
    else:
        form = ProductoForm(instance=productos)
    return render(request, 'productos/editar_producto.html', {'form': form})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listado_productos')


        