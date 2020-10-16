from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.db.models.signals import post_save


class Entity(models.Model):
    tipo_entity=[
        ('MU','Municipio'),
        ('CO', 'Cooperativa'),
        ('PL', 'Punto Limpio'),
    ]

    nombre = models.CharField(max_length=50, unique = True)
    pais = models.CharField(max_length=250, blank = True, null = True)
    prov = models.CharField('Provincia', max_length=50, blank = True, null = True)
    loc = models.CharField('Localidad', max_length=50, null = True, blank = True)
    tipo = models.CharField(choices = tipo_entity, max_length=2,default = '')   
    
    def __str__(self):
        return self.nombre

class ProfileMun(models.Model):
    tipo_dispo = [
        ('VE','Vertedero'),
        ('VC','Vertedero Controlado'),
        ('RS','Relleno Sanitario'),
    ]
    mun = models.OneToOneField(Entity, on_delete=models.CASCADE, unique = True)
    hab = models.IntegerField()
    dispo_final = models.CharField(choices = tipo_dispo, max_length=2)
    difreco = models.BooleanField(default= False)
    complejo_tratamiento = models.BooleanField(default= False)
    compostaje_biodigestion = models.BooleanField(default=False)
    planta_clasif =models.BooleanField(default=False)
    otros = models.BooleanField(default=False)
    #estadisticas
    pers_clas = models.IntegerField()
    ton_recup = models.DecimalField( max_digits=5, decimal_places=2)
    pers_recol = models.IntegerField(default=0, null=True)
    pers_comp_am = models.IntegerField()
    ton_proces = models.DecimalField( max_digits=5, decimal_places=2)
    cost_recol = models.DecimalField( max_digits=20, decimal_places=2)
    cost_comp_am = models.DecimalField( max_digits=20, decimal_places=2)
    ing_venta = models.DecimalField( max_digits=20, decimal_places=2)
    
    def __str__(self):
        return self.mun

class ProfileCop(models.Model):
    fuente_rec = [
        ('IN', 'Industria/Privado'),
        ('DO', 'Domiciliario'),
        ('MI', 'Mix'),
    ]
    cop = models.OneToOneField(Entity, on_delete=models.CASCADE, unique = True)
    cant_socio = models.IntegerField()
    fuent_rec = models.CharField( choices = fuente_rec ,max_length=2)
    recol = models.BooleanField( default=False)
    empl = models.IntegerField()
    ton_rec = models.DecimalField( max_digits=10, decimal_places=2)
    ton_a_rechazo = models.DecimalField( max_digits=10, decimal_places=2)
    gast_totales = models.DecimalField( max_digits=10, decimal_places=2)

class ProfilePunt(models.Model):
    prop = [
        ('ES', 'Estado'),
        ('PR','Privada'),
    ]
    oper = [
        ('MU', 'Municipal'),
        ('PR','Privada'),
    ]

    punt = models.ForeignKey(Entity, on_delete=models.CASCADE)
    propiedad = models.CharField('Propiedad del estado o privado', choices = prop , max_length=50)
    operacion = models.CharField('Operación municipal o privada', choices = oper , max_length=50)
    ton_recup = models.DecimalField( max_digits=10, decimal_places=2)
    visitas = models.PositiveIntegerField('Cantidad de visitas por año')
    gast_op = models.DecimalField( max_digits=10, decimal_places=2)
    cant_personas = models.IntegerField()
    fecha = models.DateTimeField(auto_now=False, auto_now_add=True)


class UserCustom(AbstractUser):
    entity = models.ForeignKey(Entity,on_delete=models.CASCADE, null = True)
    is_admin_entity = models.BooleanField(default=False)
    is_user_entity = models.BooleanField(default=False)


g_admin_entity , gae = Group.objects.get_or_create(name = 'GroupAdminEntity')
g_user_entity , gue = Group.objects.get_or_create(name = 'GroupUserEntity')

@receiver(post_save, sender = UserCustom)
def post_create(sender, instance, **kwargs):
    if instance.is_admin_entity == True:
        g_admin_entity.user_set.add(instance)
    elif instance.is_user_entity == True:
        g_user_entity.user_set.add(instance)





