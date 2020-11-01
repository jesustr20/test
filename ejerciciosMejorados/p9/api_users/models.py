from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import UserManager, Permission
from django.utils import timezone
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import (check_password, is_password_usable, make_password)

# Create your models here.

#Funcion passwordHashed generara el password y lo encriptara dentro del panel admin de django
class PasswordHashed():
    #password = models.CharField(('password'),max_length=150), recibe cualquier tipoi de parametros
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password
    
    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash considera los cambios del password encriptado
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

#Creamos el modelo el cual vamos a obtener los parametros de la tabla "auth"
class Usuario(PasswordHashed, models.Model):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=150, unique=True, validators=[username_validator])
    first_name = models.CharField(('first name'), max_length=150, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    email = models.EmailField(('email address'), blank=True)
    password = models.CharField(('password'),max_length=150)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    last_login = models.DateTimeField(('last login'), blank=True, null=True)


    _password = None
    #LLama al objeto usermanager reutilizando la funcion
    objects = UserManager()
    #EMAIL_FIELD requiere de un email obligatorio
    EMAIL_FIELD = 'email'
    #USERNAME_FIELD requiere de un email obligatorio
    USERNAME_FIELD = 'username'
    #OTROS CAMPOS REQUERIDOS
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    class Meta:
        #Falso porque no hara una operacion usando obligatoriamente el managed
        managed = False
        #Parametros usados de la tabla user
        db_table= 'auth_user'
        verbose_name = 'Adminuser'
        verbose_name_plural = 'Adminusers'
        #Falso porque la clase no sera abstracta
        abstract = False
