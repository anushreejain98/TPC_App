from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth import login
import os
from django.contrib.auth import views as auth_views
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.template import RequestContext
from .models import Student, User, Company, JobPosition
from .forms import StudentSignUpForm, CompanySignUpForm, StudentUpdateProfile,CreatePositionForm
from .models import Student, User, Company
from .forms import EditStudentForm, EditCompanyForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

#class DetailView(generic.DetailView):
#   template_name = 'home.html'

def detail(request):
    template_name = 'home.html'
    student_template = 'student/studhome.html'
    company_template = 'company/comphome.html'
    if request.user.is_authenticated:
        if request.user.is_student:
            template_name = student_template
            query = Company.objects.all().values()
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

def student_profile(request):
    return render(request, 'student/profile/student_profile.html')

def company_profile(request):
    return render(request, 'company/profile/company_profile.html')

def student_update_profile(request):
    args={}
    stud = request.user.student
    if request.method == 'POST':
        form = EditStudentForm(request.POST, instance=stud)
        if form.is_valid():
            form.save()
            return render(request, 'student/profile/profile_updated.html')
    else:
        form = EditStudentForm(instance=stud)

    args['form'] = form
    return render(request, 'student/profile/student_update_profile.html', args)

def company_update_profile(request):
    args={}
    comp = request.user.company
    if request.method == 'POST':
        form = EditCompanyForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
            return render(request, 'company/profile/profile_updated.html')
    else:
        form = EditCompanyForm(instance=comp)

    args['form'] = form
    return render(request, 'company/profile/company_update_profile.html', args)

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




class CreatePositionView(CreateView):
    model = JobPosition
    form_class = CreatePositionForm
    template_name = 'company/createjob.html'

    def job_pos_view(request):
        if request.method == 'POST':
            form = CreatePositionForm(request.POST)
            if form.is_valid():
                pos_name = form.cleaned_data.get('pos_name')
                branch_appl = form.cleaned_data.get('branch_appl')
                cpi_req = form.cleaned_data.get('cpi_req')
                course_appl = form.cleaned_data.get('course_appl')
                stipend = form.cleaned_data.get('stipend')
                ctc = form.cleaned_data.get('ctc')
                test_date = form.cleaned_data.get('test_date')
                cmp_name= request.user.company
                # do something . your results
                form.save()
                return redirect('/tpcm_app/company')

        else:
            form = CreatePositionForm()

        return render_to_response(template_name, {'form':form },
            context_instance=RequestContext(request))

    
