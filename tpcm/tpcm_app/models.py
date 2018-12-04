from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

class Student(models.Model):
    dept_choices = (('CS','CS'), ('EE','EE'), ('ME', 'ME'), ('CB', 'CB'), ('CE','CE'))
    course_choices = (('B.Tech','B.Tech'), ('M.Tech','M.Tech'), ('M.Sc','M.Sc'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name=models.CharField(max_length=30)
    cpi=models.DecimalField(max_digits=4,decimal_places=2, default='0')
    dept=models.CharField(max_length=30,default='-', choices=dept_choices)
    course=models.CharField(max_length=30,default='-', choices=course_choices)
    resume=models.URLField()
    webmail = models.EmailField(max_length=100, unique=True)
    avatar = models.ImageField(upload_to='images/', default='images/default.png')
    email = None

    def __str__(self):
        return self.name


class Company(models.Model):

    Category_choices=(('A1','A1'),('A2','A2'),('B1','B1'),)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=2,default='B1',choices=Category_choices)
    hr_name = models.CharField(max_length=30,default='-')
    hr_contact = models.EmailField(max_length=100,unique=True)
    sector = models.CharField(max_length=30, default='IT')
    email = None

    def __str__(self):
        return self.name

class JobPosition(models.Model):

    class Meta:
        unique_together=(('cmp_name','pos_name'),)

    dept_choices = (('CS','CS'), ('EE','EE'), ('ME', 'ME'), ('CB', 'CB'), ('CE','CE'))
    course_choices = (('B.Tech','B.Tech'), ('M.Tech','M.Tech'), ('M.Sc','M.Sc'))

    pos_name=models.CharField(max_length=30,help_text="This is the grey text")
    branch_appl=models.CharField(max_length=30,choices=dept_choices)
                                       
    cpi_req=models.DecimalField(max_digits=4,decimal_places=2, default='0')
    course_appl=models.CharField(max_length=30,choices=course_choices)                      
    stipend=models.IntegerField(null=True)
    ctc=models.IntegerField(null=True)
    test_date=models.DateField(null=True)
    cmp_name=models.ForeignKey(Company,on_delete=models.CASCADE,null=True)
    job_desc=models.CharField(max_length=800,null=True)
    def __str__(self):
        return self.id

class Application(models.Model):
    app_date = models.DateField(null=True)
    pos = models.ForeignKey(JobPosition, on_delete=models.CASCADE,null=True)
    stud = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.id
    class Meta:
         unique_together=(('pos','stud'),)




