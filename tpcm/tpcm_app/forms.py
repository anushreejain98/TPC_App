from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction

from .models import Student, User, Company

class StudentSignUpForm(UserCreationForm):
    id = forms.CharField(label= "Roll Number")
    name = forms.CharField(label= "Full Name")
    cpi = forms.DecimalField(label="Current CPI")
    dept = forms.CharField(label="Department")
    course = forms.CharField(label="Course of study")
    resume = forms.URLField(label="URL to resume")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("id", "name", "cpi", "dept", "course", "resume","password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.username= self.cleaned_data["id"]
        user.save()
        student = Student.objects.create(user=user)
        student.name = self.cleaned_data["name"]
        student.cpi = self.cleaned_data["cpi"]
        student.dept = self.cleaned_data["dept"]
        student.course = self.cleaned_data["course"]
        student.resume = self.cleaned_data["resume"]
        student.save()
        return user

class CompanySignUpForm(UserCreationForm):
    id = forms.CharField(label= "Company ID")
    name = forms.CharField(label= "Name of the company")
    category = forms.CharField(label="Category")
    hr_name = forms.CharField(label="Name of HR")
    hr_contact = forms.EmailField(label="HR Email")
    sector = forms.CharField(label="Sector")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("id", "name", "category", "hr_name", "hr_contact", "sector","password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.username= self.cleaned_data["id"]
        user.save()
        company = Company.objects.create(user=user)
        company.name = self.cleaned_data["name"]
        company.category = self.cleaned_data["category"]
        company.hr_name = self.cleaned_data["hr_name"]
        company.hr_contact = self.cleaned_data["hr_contact"]
        company.sector = self.cleaned_data["sector"]
        company.save()
        return user

class StudentLoginForm(AuthenticationForm):
    username = forms.CharField(label= "Roll no")
    def confirm_login_allowed(self, user):
        pass

class CompanyLoginForm(AuthenticationForm):
    username = forms.CharField(label= "Company ID")
    def confirm_login_allowed(self, user):
        pass