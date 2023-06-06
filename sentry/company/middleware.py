from django.contrib import messages
from sentry.company.models import Domain
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout as auth_logout


class CompanyAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            # Verifica si el usuario está autenticado y pertenece a una empresa
            if request.user.is_authenticated and request.user.company is not None:
                company_domain = Domain.objects.get(id=request.user.company.id)
                request_domain = request.get_host().split(':')[0]
                if request_domain != company_domain.domain:
                    auth_logout(request)
                    messages.error(request, 'Credenciales incorrectas. Ingrese el dominio correcto.')
                    return redirect('admin:login')
        return self.get_response(request)
