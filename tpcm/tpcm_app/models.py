from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=30)
    Roll_no=models.CharField(max_length=8)
    CPI=models.DecimalField(max_digits=4,decimal_places=2)
    Dept=models.CharField(max_length=30,default='-')
    Course=models.CharField(max_length=30,default='-')
    Resume=models.URLField()

    def __str__(self):
        return self.Name


class Company(models.Model):
    A1='A1'
    A2='A2'
    B1='B1'
    #Category_choices=((A1,'A1'),(A2,'A2'),(B1,'B1'),)

    Name = models.CharField(max_length=30)
    Category=models.CharField(max_length=2,default='B1')
    HR_name = models.CharField(max_length=30,default='-')
    HR_contact = models.EmailField(max_length=100,unique=True)
    Sector=models.CharField(max_length=30, default='IT')

    def __str__(self):
        return self.Name



