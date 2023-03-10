from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, email, first_name, last_name, telephone, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            telephone=telephone,
            rol=Rol.objects.get(id=1),
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, first_name, last_name, telephone, password=None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, telephone, password, False, False, **extra_fields)
    
    def create_superuser(self, username, email, first_name, last_name, telephone, password=None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, telephone, password, True, True, **extra_fields)

class Rol(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    name = models.CharField(max_length=200, verbose_name="Nombre Rol")

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True, verbose_name="Nombre de Usuario")
    email = models.EmailField(max_length=254, unique=True, verbose_name="Correo electronico")
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Rol")
    telephone = models.CharField(max_length=100, verbose_name="Telefono")
    picture = models.ImageField(upload_to='perfil/', max_length=200, blank=True, null=True, verbose_name="Foto de perfil")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name',
        'telephone',
    ]

    def __str__(self):
        return self.username
