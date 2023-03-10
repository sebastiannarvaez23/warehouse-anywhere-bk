from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, telephone, rol, picture=None, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            telephone=telephone,
            picture=picture,
            rol=rol
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name, telephone, password):
        user = self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            telephone=telephone,
            rol=Rol.objects.get(id=1)
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class Rol(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    name = models.CharField(max_length=200, verbose_name="Nombre Rol")

class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True, verbose_name="Nombre de Usuario")
    email = models.EmailField(max_length=254, unique=True, verbose_name="Correo electronico")
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Rol")
    telephone = models.CharField(max_length=100, verbose_name="Telefono")
    picture = models.ImageField(upload_to='perfil/', max_length=200, blank=True, null=True, verbose_name="Foto de perfil")
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
    
    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.rol = Rol.objects.get(id=1)
        elif not self.rol:
            self.rol = Rol.objects.get(id=2)
        super().save(*args, **kwargs)
