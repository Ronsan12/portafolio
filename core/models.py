from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    imagen = models.ImageField(
        upload_to='projects/'
    )

    github = models.URLField()

    video_demo = models.URLField()

    tecnologias = models.CharField(
        max_length=200
    )

    destacado = models.BooleanField(
        default=False
    )

    fecha_creacion = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nombre