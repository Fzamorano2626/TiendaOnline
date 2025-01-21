from django.db import models

# Create your models here.

# creamos el modelo de base de datos que va a tener la aplicación
# Creamos nuestra primera clase para crear la primera tabla (por cada clase se crea una tabla)

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name='La Dirección')
    email=models.EmailField(blank=True, null=True)
    tfno=models.CharField(max_length=7)
    
    def __str__(self):
         return self.nombre
    
    
class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    sesion=models.CharField(max_length=20)
    precio=models.IntegerField()
    
    def __str__(self):
             return 'El Nombre es %s La Sección es %s El Precio es %s' %(self.nombre, self.sesion, self.precio)
         
class Pedidos(models.Model):
    numero=models.IntegerField(verbose_name='Numero de Pedido')#verbose es para ca,biar el nombre a mostrar en el panel de admin
    fecha=models.DateField()
    entregado=models.BooleanField()
         
                  
         
         
    

    
