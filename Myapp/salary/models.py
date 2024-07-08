from django.db import models
from django.core.validators import * 


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    telephone = RegexValidator(regex=r'^\+251?1?\d{9,15}$')
    phone_number = models.CharField(validators=[telephone, MaxLengthValidator],max_length=20)
    gender = models.CharField(max_length=10, choices=[('M','M'), ('F', 'F')] , default='N')
    salary = models.DecimalField(max_digits=8,decimal_places=2,default=0.00)
