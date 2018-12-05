from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
app_name='tpcm_app'
from .models import Student, User, Company, JobPosition
from . import views
from .forms import StudentLoginForm, CompanyLoginForm,CreatePositionForm
urlpatterns = [
    
    #/tpcm_app/
    #url(r'^$',views.detail,name='detail'),
    #url(r'student/$',views.stud,name='stud'),
    #url(r'company/$',views.cmp,name='cmp'),
    path('', views.detail, name='home'),
    path('login/type/', views.login_type, name='logintype'),
    path('signup/type/', views.signup_type, name='signuptype'),
    path('signup/student/', views.StudentSignUpView.as_view(), name='stud'),
    path('signup/company', views.CompanySignUpView.as_view(), name='cmp'),
    path('login/student', auth_views.LoginView.as_view(template_name="login/studentlogin.html"
    , authentication_form=StudentLoginForm), name='slogin'),
    path('login/company', auth_views.LoginView.as_view(template_name="login/companylogin.html"
    , authentication_form=CompanyLoginForm), name='clogin'),
    path('signout/', auth_views.LogoutView.as_view(template_name="home.html"), name='signout'),
    path('student/profile/update', views.student_update_profile, name='student_update'),
    path('student/profile', views.student_profile, name='student_profile'),
    path('contact/', views.contact, name='contact'),
    path('company/profile/update', views.company_update_profile, name='company_update'),
    path('company/profile', views.company_profile, name='company_profile'),
    path('company/createjob',views.create_job,name='cmp_createjob'),
    path('student/position/apply', views.apply_pos, name='apply_pos'),
    path('student/position/desc', views.desc_pos, name='desc_pos'),
    path('student/position/apply/success', views.apply_success, name='apply_success'),
    path('student/myapplications', views.student_view_applications, name='student_applications'),
    path('company/positions',views.positions,name='positions'),
    path('company/positions/close',views.close_positions,name='close_positions'),
    path('company/application',views.list_application,name='list_application'),
    path('company/application/close',views.close_application,name='close_application'),
    path('company/application/stud_profile', views.stud_profile, name='stud_profile'),
    path('company/application/desc',views.show_position,name='views.show_position'),
]
