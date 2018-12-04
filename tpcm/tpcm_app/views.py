from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth import login
import os
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import views as auth_views
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.template import RequestContext
from .models import Student, User, Company, JobPosition, Application
from .forms import StudentSignUpForm, CompanySignUpForm, CreatePositionForm,EditStudentForm, EditCompanyForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from .decorators import student_required, company_required
import datetime

def detail(request):
    template_name = 'home.html'
    student_template = 'student/studhome.html'
    company_template = 'company/comphome.html'
    if request.user.is_authenticated:
        if request.user.is_student:
            template_name = student_template
            query = JobPosition.objects.all().select_related('cmp_name')
            return render(request, template_name, context={
                "username":request.user.student.name,
                "query":query,
                })
        else:
            template_name = company_template
            return render(request, template_name, context={"username":request.user.company.name})

    return render(request,template_name)

def contact(request):
    return render(request, 'contact.html')
def login_type(request):
    return render(request,'login/logintype.html')

def signup_type(request):
    return render(request, 'signup/signuptype.html')

@login_required
@student_required
def student_profile(request):
    args={'username':request.user.student.name}
    return render(request, 'student/profile/student_profile.html', args)

@login_required
@company_required
def company_profile(request):
    args={'username':request.user.company.name}
    return render(request, 'company/profile/company_profile.html', args)

@login_required
@company_required
def positions(request):
    comp = request.user.company
    query = JobPosition.objects.all().select_related('cmp_name').filter(cmp_name=comp)
    return render(request, 'company/job/positions.html', context={
        "query":query,'username':request.user.company.name}
        )

@login_required
@company_required
def list_application(request):
    pos=request.GET.get('id', '')
    if pos == '':
        query = Application.objects.all().select_related('pos').select_related('stud')
    else:
        query = Application.objects.all().select_related('pos').select_related('stud').filter(pos_id=pos)
    return render(request, 'company/job/applications.html', context={
        "query":query,'username':request.user.company.name}
        )

def stud_profile(request):
    stud_id = request.GET.get('id')
    query = User.objects.all().filter(student__user_id=stud_id)
    return render(request, 'company/job/stud_profile.html', context={
        "query":query,'username':request.user.company.name
    })

@login_required
@student_required
def student_update_profile(request):
    args={'username':request.user.student.name}
    stud = request.user.student
    if request.method == 'POST':
        form = EditStudentForm(request.POST, instance=stud)
        if form.is_valid():
            form.save()
            return render(request, 'student/profile/profile_updated.html', args)
    else:
        form = EditStudentForm(instance=stud)

    args['form'] = form
    return render(request, 'student/profile/student_update_profile.html', args)

@login_required
@company_required
def company_update_profile(request):
    args={'username':request.user.company.name}
    comp = request.user.company
    if request.method == 'POST':
        form = EditCompanyForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
            return render(request, 'company/profile/profile_updated.html', args)
    else:
        form = EditCompanyForm(instance=comp)
    args['form'] = form
    return render(request, 'company/profile/company_update_profile.html', args)

@login_required
@company_required
def create_job(request):
    ini={'cmp_name':request.user.company}
    if request.method=='POST':
        form=CreatePositionForm(request.POST, initial=ini)

        if form.is_valid():
            form.save()
            template_name = 'company/job/job_created.html'
            query = JobPosition.objects.all().values()
            return render(request, template_name, context={
                "query":query, 'username':request.user.company.name
                })              
    else:
        form=CreatePositionForm(initial=ini)
    
    return render(request,'company/job/createjob.html',
        {
            'form':form, 
            'username':request.user.company.name
        }
    )

@login_required
@student_required
def desc_pos(request):
    pos_id = request.GET.get('id')
    query = JobPosition.objects.get(id=pos_id)
    username = request.user.student.name
    return render(request, 'student/position/description.html', context={'query':query,
    'username':username})

@login_required
@student_required
def apply_pos(request):
    pos_id = request.GET.get('id')
    job_pos = JobPosition.objects.get(id=pos_id)
    stud = request.user.student
    app = Application.objects.create(pos=job_pos, stud=stud, app_date=datetime.date.today())
    app.save()
    return redirect('/tpcm_app/student/position/apply/success')

@login_required
@student_required
def apply_success(request):
    args={'username':request.user.student.name}
    return render(request, 'student/position/success.html', args)


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'signup/studentsignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/tpcm_app/')


class CompanySignUpView(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = 'signup/companysignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/tpcm_app/')

