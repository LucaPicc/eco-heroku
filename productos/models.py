from django.db import models
from user.models import Entity, UserCustom

class Material(models.Model):
    nombre = models.CharField('Nombre del material', max_length=50)
    descripcion = models.CharField('Breve descripcion del material', max_length=250)

    def __str__(self):
        return self.nombre
        
class MaterialStock(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, unique = False)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, unique = False)
    peso = models.DecimalField( max_digits=5, decimal_places=2, default = 0)


class Product(models.Model):
    nombre = models.CharField("Nombre de producto", max_length=50)
    descripcion = models.CharField("Descripción de producto", max_length=250, default = '',null = True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE,unique = False)
    cantkg = models.DecimalField(max_digits = 5, decimal_places = 3, default = 0)

    def __str__(self):
        return self.nombre

class ProductStock(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, unique = False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, unique = False)
    cantidad = models.IntegerField()

class MovPStock(models.Model):
    t_mov = [
        ('EP','Entrada de Producto'),
        ('SP', 'Salida de Producto'),
    ]
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    usuario = models.ForeignKey( UserCustom, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    peso = models.IntegerField()
    tipo = models.CharField(choices= t_mov, max_length=2)
    fecha = models.DateTimeField( auto_now=False, auto_now_add=True)

class MovMStock(models.Model):
    t_mov = [
        ('EM','Entrada de Material'),
        ('SM', 'Salida de Material'),
    ]
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    usuario = models.ForeignKey( UserCustom, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    peso = models.IntegerField()
    tipo = models.CharField(choices= t_mov, max_length=2)
    fecha = models.DateTimeField( auto_now=False, auto_now_add=True)


class SendProduct(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, blank=False, null = False)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, blank=False, null = False)
    cant = models.IntegerField()
    date_env = models.DateTimeField( auto_now=False, auto_now_add=True)
    date_recp = models.DateField(auto_now=True, auto_now_add=False)
    recp = models.BooleanField(default=False)

class SendMaterial(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, blank=False, null = False)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, blank=False, null = False)
    cant = models.IntegerField()
    date_env = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_recp = models.DateField(auto_now=True, auto_now_add=False)
    recp = models.BooleanField(default = False)
