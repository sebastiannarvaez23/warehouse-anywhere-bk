from django.db import models
from django_tenants.models import DomainMixin, TenantMixin

# Create your models here.    
class Company(TenantMixin):
    id = models.AutoField(primary_key=True)
    nit = models.CharField(max_length=40)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    created = models.DateField(auto_now=True)

    auto_create_schema = True
    
    def __str__(self):
        return self.name
    
class Domain(DomainMixin):
    pass