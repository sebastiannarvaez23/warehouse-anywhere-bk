from django.db import models

# Create your models here.
class Color(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Reference(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    item_code = models.CharField(max_length=100, verbose_name="Código")
    name = models.CharField(max_length=255, verbose_name="Referencia")
    model_size = models.CharField(max_length=100, verbose_name="Talla")
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Referencia"
        verbose_name_plural = "Referencias"
        ordering = ['-id']

    def __str__(self):
        return self.item_code

class PropertyHeader(models.Model):
    id = models.AutoField(primary_key=True)
    header = models.CharField(max_length=200)
    reference = models.ForeignKey(Reference, on_delete=models.DO_NOTHING)

class PropertyContent(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    header = models.ForeignKey(PropertyHeader, on_delete=models.DO_NOTHING)