from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 200)

    def __str__(self):
        return self.nombre

#Para migrar esto a una bd hay que regresar a
#donde se encuentra manage.py
#ejecutar el comando "python manage.py makemigrations"
#ademas colocar en installed apps
#Para aplicarlo a la bd el comando es "python manage.py migrate"
#Agregar a admin.py para que aparezca en el admin

#Para enviar esto al template se envia a traves de contexto