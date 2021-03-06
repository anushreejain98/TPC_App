from .models import Student, User, Company, JobPosition
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.db import transaction
import datetime

class StudentSignUpForm(UserCreationForm):
    dept_choices = (('CS','CS'), ('EE','EE'), ('ME', 'ME'), ('CB', 'CB'), ('CE','CE'))
    course_choices = (('B.Tech','B.Tech'), ('M.Tech','M.Tech'), ('M.Sc','M.Sc'))
    username = forms.CharField(label= "Roll Number")
    name = forms.CharField(label= "Full Name")
    cpi = forms.DecimalField(label="Current CPI")
    dept = forms.CharField(label="Department", widget=forms.Select(choices=dept_choices))
    course = forms.CharField(label="Course of study", widget=forms.Select(choices=course_choices))
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
        student.webmail = self.cleaned_data["webmail"]
        student.save()
        return user

class CompanySignUpForm(UserCreationForm):
    Category_choices=(('A1','A1'),('A2','A2'),('B1','B1'),)
    username = forms.CharField(label= "Company ID")
    name = forms.CharField(label= "Name of the company")
    category = forms.CharField(label="Category",widget=forms.Select(choices=Category_choices))
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

class EditStudentForm(UserChangeForm):
    password = None
    class Meta:
        model = Student
        fields = ("name", "cpi", "dept", "course", "resume", "avatar")


class CreatePositionForm(forms.ModelForm):
    dept_choices = (('CS','CS'), ('EE','EE'), ('ME', 'ME'), ('CB', 'CB'), ('CE','CE'))
    course_choices = (('B.Tech','B.Tech'), ('M.Tech','M.Tech'), ('M.Sc','M.Sc'))     
    pos_name=forms.CharField(label="Job Position")
    branch_appl=forms.CharField(widget=forms.Select(choices=dept_choices))                                   
    cpi_req=forms.DecimalField(label="Min. CPI required")
    course_appl=forms.CharField(label="Select Course",
                                widget=forms.Select(choices=course_choices))
    stipend=forms.IntegerField(label="Stipend")
    ctc=forms.IntegerField(label="CTC")
    job_desc=forms.CharField(label="Job Description",widget=forms.Textarea)

    class Meta:
        model = JobPosition
        fields = ('pos_name', 'branch_appl', 'cpi_req', 'course_appl',
                'stipend','ctc','test_date','job_desc', 'cmp_name')
        widgets = {'test_date': forms.DateInput(format=('%m/%d/%Y'),
                    attrs={'class':'datepicker', 'placeholder':'Select a date', 'type':'date'}),
                    'cmp_name': forms.HiddenInput
                    }
     

class EditCompanyForm(UserChangeForm):
    password = None
    class Meta:
        model = Company
        fields = ("hr_name", "hr_contact", "category", "sector")
