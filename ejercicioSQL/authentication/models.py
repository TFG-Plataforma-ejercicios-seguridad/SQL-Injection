from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import  MinValueValidator
# Create your models here.

class Employee(AbstractUser):
    role = models.CharField(max_length=255,verbose_name='Rol')
    business_department = models.CharField(max_length=255,verbose_name='Departamento de la Empresa')
    salary = models.FloatField(validators=[MinValueValidator(0.0)])
    
class AuthorizationCode(models.Model):
    flag = models.CharField(max_length=255,verbose_name='Bandera')