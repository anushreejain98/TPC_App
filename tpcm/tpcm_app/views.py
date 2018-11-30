from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth import login
import os
from django.contrib.auth import views as auth_views
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.template import RequestContext
from .models import Student, User, Company
from .forms import StudentSignUpForm, CompanySignUpForm, StudentUpdateProfile
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

def login_type(request):
    return render(request,'login/logintype.html')

def signup_type(request):
    return render(request, 'signup/signuptype.html')

def student_profile(request):
    return render(request, 'student/profile/student_profile.html')

def student_update_profile(request):
    args = {}
    if request.method == 'POST':
        form = StudentUpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'student/profile/profile_updated.html')
    else:
        form = StudentUpdateProfile()

    args['form'] = form
    return render(request, 'student/profile/student_update_profile.html', args)

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




