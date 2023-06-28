from django.db import models

# Create your models here.

HORARIO = [
        (1, "10:00 AM"),
        (2, "12:00 PM"),
        (3, "2:00 PM"),
        (4, "4:00 PM"),
        (5, "6:00 PM"),
    ]

class persona(models.Model):
    rut=models.CharField(primary_key=True, null=False, max_length=10,error_messages="Debe ingresar rut")
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
@classmethod
def obtener_por_id(cls, persona_id):
    return cls.objects.get(id=persona_id)

    
class pelicula(models.Model):
    nombrePeli=models.CharField(max_length=50, null=False)
    descripcion=models.CharField(max_length=500,  null=False)
    credYreparto=models.CharField(max_length=50, null=False)
    portada=models.ImageField(upload_to="portadas", null=True)
    linkTrailer=models.CharField(max_length=500, null=True)


class compraBoleto(models.Model):
    nombrePeli=models.ForeignKey(pelicula, on_delete=models.PROTECT,null=False)
    horario=models.CharField(max_length=1, choices=HORARIO)
    cantidad = models.IntegerField()
    f_compra=models.DateField()