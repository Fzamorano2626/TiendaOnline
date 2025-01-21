from django.contrib import admin

# Register your models here.
# Importo los modelos

from gestionPedidos.models import Clientes, Articulos, Pedidos

#creo una clase que permita mostrar mas campos desde el panel de admin din crear la clase desde el modelo

class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre', 'direccion', 'tfno')
    #agrego casilla de busquedad
    search_fields=('nombre', 'tfno')
    
#Creamos una clase para colocar el filtro de busquedad en la tabla Articulos del Admin   
class ArticulosAdmin(admin.ModelAdmin):
    list_filter=('sesion', 'precio',)# se agrega como al final por ser una tupla
    
#Creamos una clase para colocar el filtro de busquedad por fecha en Pedidos   
class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero', 'fecha') 
    list_filter=('fecha',)# se agrega como al final por ser una tupla   
    date_hierarchy=('fecha')#para mostrar el filtro en el menu horizontal
    

# se incluye para que desde el panel tengamos las tablas disponibles
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)



