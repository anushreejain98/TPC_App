from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth import login
import os

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.template import RequestContext
from .models import Student, User
from .forms import StudentSignUpForm, CompanySignUpForm
from django.contrib.auth import authenticate, login, logout

#class DetailView(generic.DetailView):
#   template_name = 'home.html'

def detail(request):
    template_name = 'home.html'
    student_template = 'studhome.html'
    company_template = 'comphome.html'
    if request.user.is_authenticated:
        if request.user.is_student:
            template_name = student_template
            return render(request, template_name, context={"username":request.user.student.name})
        else:
            template_name = company_template
            return render(request, template_name, context={"username":request.user.company.name})

    return render(request,template_name)

def login_type(request):
    return render(request,'login/logintype.html')
def signup_type(request):
    return render(request, 'signup/signuptype.html')

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


