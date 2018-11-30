from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name=models.CharField(max_length=30)
    cpi=models.DecimalField(max_digits=4,decimal_places=2, default='0')
    dept=models.CharField(max_length=30,default='-')
    course=models.CharField(max_length=30,default='-')
    resume=models.URLField()
    webmail = models.EmailField(max_length=100, unique=True)
    avatar = models.ImageField(upload_to='images/', default='images/default.png')

    def __str__(self):
        return self.name


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
    date_of_visit = models.DateField(null=True)

    def __str__(self):
        return self.name

class JobPosition(models.Model):
    DEPT=(("CSE","Computer Science"),
        ("EE","Electrical"),
        ("ME","Mechanical"),
        ("CE","Civil Engg."),
        ("CB","Chemical Engg."),)

    COURSE=[('btech','B. Tech'),
            ('mtech','M. Tech'),]

    pos_name=models.CharField(max_length=30)
    branch_appl=models.CharField(max_length=30,choices=DEPT)
                                       
    cpi_req=models.DecimalField(max_digits=4,decimal_places=2, default='0')
    course_appl=models.CharField(max_length=30,choices=COURSE)
                                
    stipend=models.IntegerField(null=True)
    ctc=models.IntegerField(null=True)
    test_date=models.DateField(null=True)
    cmp_name=models.ForeignKey(Company,on_delete=models.CASCADE,)

    def __str__(self):
        return self.pos_name + '   ' + self.cmp_name




