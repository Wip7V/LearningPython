from django.db import models
from django.urls import reverse

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=150,help_text="Nombre completo del director")
    day_of_birth = models.DateField(null=True, blank=True)
    day_of_death = models.DateField(null=True, blank=True)
    image = models.URLField(null=True)
   
    def __str__(self):
        return '%s' % (self.name)

class Film(models.Model):
    title = models.CharField(max_length=150, help_text="Nombre de la película")
    release_date = models.DateField(null=True, blank=True)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, help_text="Descripción de la película")
    image = models.URLField(null=True)

    def __str__(self):
        return self.title


