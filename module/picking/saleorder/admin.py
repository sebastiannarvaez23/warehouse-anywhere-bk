from django.contrib import admin
from rest_framework.exceptions import PermissionDenied
from .models import Collection, SaleOrder, PayTerm

admin.site.register(SaleOrder)
admin.site.register(Collection)
admin.site.register(PayTerm)
