

from django.shortcuts import render
import os

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView

from .models import Student,Company

#class DetailView(generic.DetailView):
#   template_name = 'home.html'

def detail(request):
	return render(request,'home.html')

def stud(request):
	return render(request,'student.html')
 
def cmp(request):
	return render(request,'company.html')