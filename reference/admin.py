from django.contrib import admin
from .models import Reference, Color, PropertyHeader, PropertyContent

# Register your models here.
admin.site.register(Reference)
admin.site.register(Color)
admin.site.register(PropertyHeader)
admin.site.register(PropertyContent)