from django.db import models

# Create your models here.
class Categoria(models.Model):
    id  = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

class Deporte(models.Model):
    id  = models.IntegerField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class Planes(models.Model):
    id  = models.IntegerField(primary_key=True)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    precioMensual= models.CharField(max_length=40)
    precioSemestral= models.CharField(max_length=40)
    precioAnual= models.CharField(max_length=40)
    activo = models.BooleanField()

class Clientes(models.Model):
    id  = models.IntegerField(primary_key=True)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    rut = models.CharField(max_length=10,verbose_name="rut completo")
    nombre = models.CharField(max_length=40)
    paterno = models.CharField(max_length=40,verbose_name="Apellido Paterno")
    materno= models.CharField(max_length=40)
    fechaNac = models.CharField(max_length=40)
    genero = models.BooleanField()
    email=models.CharField(max_length=60)
    telefono=models.CharField(max_length=40)
    ofertaSino=models.BooleanField()
    activo = models.BooleanField()


    def __str__(self):
        return self.nombre