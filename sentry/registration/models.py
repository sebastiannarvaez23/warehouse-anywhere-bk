from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from sentry.company.models import Company
# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, email, first_name, last_name, telephone, company, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            telephone=telephone,
            rol=Rol.objects.get_or_create(name='Administrador Tecnologico')[0],
            company=Company.objects.get(id=company),
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, first_name, last_name, telephone, company, password=None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, telephone, company, password, False, False, **extra_fields)
    
    def create_superuser(self, username, email, first_name, last_name, telephone, company, password=None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, telephone, company, password, True, True, **extra_fields)

class Rol(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    name = models.CharField(max_length=200, verbose_name="Nombre Rol")

    def __str__(self):
        return self.name

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True, verbose_name="Nombre de Usuario")
    email = models.EmailField(max_length=254, unique=True, verbose_name="Correo electronico")
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=100, verbose_name="Telefono")
    picture = models.ImageField(upload_to='perfil/', max_length=200, blank=True, null=True, verbose_name="Foto de perfil")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name',
        'telephone',
        'company'
    ]

    def __str__(self):
        return self.username
