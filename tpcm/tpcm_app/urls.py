
from django.conf.urls import url
from django.contrib import admin

app_name='tpcm_app'

from . import views

urlpatterns = [
    
    #/tpcm_app/
    url(r'^$',views.detail,name='detail'),
    url(r'student/$',views.stud,name='stud'),
    url(r'company/$',views.cmp,name='cmp'),
]