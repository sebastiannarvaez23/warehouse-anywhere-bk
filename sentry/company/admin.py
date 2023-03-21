from django.contrib import admin
from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from sentry.company.models import Company

@admin.register(Company)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('schema_name', 'name')