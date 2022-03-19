from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.response import Response
from tunniplaan import getnextlesson
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'tunniplaan/index.html'
    context_object_name = 'info'

    def get_queryset(self):
        return getnextlesson.getnextlesson()