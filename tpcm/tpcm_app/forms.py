from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction

from .models import Student, User, Company, JobPosition
import datetime

class StudentSignUpForm(UserCreationForm):
    username = forms.CharField(label= "Roll Number")
    name = forms.CharField(label= "Full Name")
    cpi = forms.DecimalField(label="Current CPI")
    dept = forms.CharField(label="Department")
    course = forms.CharField(label="Course of study")
    resume = forms.URLField(label="URL to resume")
    webmail = forms.EmailField(label="Webmail ID")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "name", "cpi", "dept", "course", "resume", "webmail", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.username= self.cleaned_data["username"]
        user.save()
        student = Student.objects.create(user=user)
        student.name = self.cleaned_data["name"]
        student.cpi = self.cleaned_data["cpi"]
        student.dept = self.cleaned_data["dept"]
        student.course = self.cleaned_data["course"]
        student.resume = self.cleaned_data["resume"]
        student.email = self.cleaned_data["webmail"]
        student.save()
        return user

class CompanySignUpForm(UserCreationForm):
    username = forms.CharField(label= "Company ID")
    name = forms.CharField(label= "Name of the company")
    category = forms.CharField(label="Category")
    hr_name = forms.CharField(label="Name of HR")
    hr_contact = forms.EmailField(label="HR Email")
    sector = forms.CharField(label="Sector")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "name", "category", "hr_name", "hr_contact", "sector","password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.username= self.cleaned_data["username"]
        user.save()
        company = Company.objects.create(user=user)
        company.name = self.cleaned_data["name"]
        company.category = self.cleaned_data["category"]
        company.hr_name = self.cleaned_data["hr_name"]
        company.hr_contact = self.cleaned_data["hr_contact"]
        company.sector = self.cleaned_data["sector"]
        company.date_of_visit = datetime.date.today()
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

class StudentUpdateProfile(forms.ModelForm):
    name = forms.CharField(label= "Full Name", required=False)
    cpi = forms.DecimalField(label="Current CPI", required=False)
    dept = forms.CharField(label="Department", required=False)
    course = forms.CharField(label="Course of study", required=False)
    resume = forms.URLField(label="URL to resume", required=False)
    webmail = forms.EmailField(label="Webmail ID", required=False)
    class Meta:
        model = User
        fields = ('name', 'cpi', 'dept', 'course', 'resume', 'webmail')

    def clean_email(self):
        webmail = self.cleaned_data.get('webmail')

        if webmail and Student.objects.filter(webmail='webmail').count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return webmail

    def save(self, commit=True):
        user = super(StudentUpdateProfile, self).save(commit=False)
        user.student.webmail = self.clean_email()
        user.student.name = self.cleaned_data.get('name')
        user.student.cpi = self.cleaned_data.get('cpi')
        user.student.resume = self.cleaned_data.get('resume')
        user.student.dept = self.cleaned_data.get('dept')
        user.student.course = self.cleaned_data.get('course')
        user.save()
        return user


class CreatePositionForm(forms.ModelForm):
    DEPT=(("CSE","Computer Science"),
        ("EE","Electrical"),
        ("ME","Mechanical"),
        ("CE","Civil Engg."),
        ("CB","Chemical Engg."),)

    COURSE=[('btech','B. Tech'),
            ('mtech','M. Tech'),]
            
    pos_name=forms.CharField(label="Job Position")
    branch_appl=forms.CharField(widget=forms.CheckboxSelectMultiple(choices=DEPT))
                                        
    cpi_req=forms.DecimalField(label="Min. CPI required")
    course_appl=forms.CharField(label="Select Course",
                                widget=forms.Select(choices=COURSE))
    stipend=forms.IntegerField(label="Stipend")
    ctc=forms.IntegerField(label="CTC")
    test_date=forms.DateField(label="Online Test Date")
    
    class Meta:
        model = JobPosition
        fields = ('pos_name', 'branch_appl', 'cpi_req', 'course_appl',
                'stipend','ctc','test_date')


