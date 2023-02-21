# Django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Local apps
from picking.models import Picking

# Create your models here.
class Dimension(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    name = models.CharField(max_length=255, unique=True, verbose_name="Nombre")
    dimension_height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Dimension height ")
    dimension_width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Dimension width ")
    dimension_length = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Dimension length")
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Peso Bruto")
    
    class Meta:
        verbose_name = "Dimension"
        verbose_name_plural = "Dimensiones"
        ordering = ['id']

    def __str__(self):
        return self.name

class Box(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    last_modification = models.DateTimeField(verbose_name="Última modificación", default=timezone.now)
    gross_weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Peso Bruto")
    responsible = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Responsable")
    dimension = models.ForeignKey(Dimension, on_delete=models.DO_NOTHING, verbose_name="Dimensión")
    picking = models.ForeignKey(Picking, on_delete=models.DO_NOTHING, verbose_name="Despacho")

    class Meta:
        verbose_name = "Caja"
        verbose_name_plural = "Cajas"
        ordering = ['-last_modification']

    def __str__(self):
        return self.dimension.name

    def save(self, *args, **kwargs):
        # Actualiza la fecha y hora de la última modificación
        self.last_modification = timezone.now()
        super(Box, self).save(*args, **kwargs)
