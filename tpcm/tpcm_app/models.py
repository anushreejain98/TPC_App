from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

from .managers import UserManager
# Create your models here.

class User(AbstractUser):
    id = models.CharField(max_length=8, unique=True, primary_key=True)
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    USERNAME_FIELD = 'id'
    objects = UserManager()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name=models.CharField(max_length=30)
    cpi=models.DecimalField(max_digits=4,decimal_places=2, default='0')
    dept=models.CharField(max_length=30,default='-')
    course=models.CharField(max_length=30,default='-')
    resume=models.URLField()

    def __str__(self):
        return self.Name


class Company(models.Model):
    A1='A1'
    A2='A2'
    B1='B1'
    #Category_choices=((A1,'A1'),(A2,'A2'),(B1,'B1'),)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=2,default='B1')
    hr_name = models.CharField(max_length=30,default='-')
    hr_contact = models.EmailField(max_length=100,unique=True)
    sector = models.CharField(max_length=30, default='IT')

    def __str__(self):
        return self.Name



