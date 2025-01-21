from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    
    #Ingresamos el if / else para que controle si viene información en el formulario
    
    if request.GET["prd"]:
         
        #mensaje="Articulo Buscado: %r" %request.GET["prd"]
        
        #creamos un instrucción para buscar el dato ingresado en la DB, el icontains es un like en sql
        producto=request.GET["prd"]
        #Evaluamos la longitud de la busqueda, de los caracteres ingresados
        
        if len(producto)>20:
            
            mensaje="Texto de busquedad excede la Longitud maxima(20 Cartacteres)"
            
        else:
        
            articulos=Articulos.objects.filter(nombre__icontains=producto)
        
            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})
        
    else:
        
         mensaje="El dato no es valido"  
        
    return HttpResponse(mensaje)

#Creamos una nueva vista para crear un formulario de contacto

@csrf_exempt
def contacto(request):
    
    if request.method=="POST":
        return render(request, "gracias.html")
    
    return render(request, "contacto.html")






