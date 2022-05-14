from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView, status
from rest_framework.response import Response
from tunniplaan import getnextlesson
from django.views import generic
from tunniplaan.models import *
from tunniplaan.forms import *
def index(response):
    template_name = 'tunniplaan/index.html'
    def get_queryset():
        return getnextlesson.getnextlesson()
    form = ClassModelForm
    return render(response, template_name, {"info":get_queryset(), "form":form})
