from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse
import os


def index(request):
    template = loader.get_template("example.html")
    cwd = os.getcwd()
    print(cwd)
    return HttpResponse(template.render())

