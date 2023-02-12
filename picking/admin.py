from django.contrib import admin
from .models import Status, Picking

# Register your models here.
admin.site.register(Picking)
admin.site.register(Status)