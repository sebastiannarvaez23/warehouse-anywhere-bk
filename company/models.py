from django.db import models

# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    nit = models.CharField(max_length=40)
    name = models.CharField(max_length=200, unique=True)
    domain = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=255)
    city = models.CharField()
    
    def __str__(self):
        return self.name