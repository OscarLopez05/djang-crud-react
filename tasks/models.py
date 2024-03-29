from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    done = models.BooleanField(default = False)

    #aqui defino un metodo para poder observar el nombre de la tarea desde el apartado de admin
    def __str__(self):
        return self.title