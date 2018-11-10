from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=30)
    Roll_no=models.CharField(max_length=8)
    Department=models.CharField(max_length=30)
    CPI=models.IntegerField()
    Resume=models.URLField()

    def __str__(self):
        return self.Name

class Company(models.Model):
    Name = models.CharField(max_length=30)
    Category=models.CharField(max_length=2)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    HR_contact = models.CharField(validators=[phone_regex], max_length=17,
                                    blank=True)  # validators should be a list  JAF_link=models.URLField(null=True)

    def __str__(self):
        return self.Name



