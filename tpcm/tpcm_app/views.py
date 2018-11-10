from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse
import os


def index(request):
    cwd = os.getcwd()
    print(cwd)
    template = loader.get_template("example.html")
    return HttpResponse(template.render())


