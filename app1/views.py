from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def muni(request):
    return HttpResponse('hellow world')

def muni1(request):
    return HttpResponse('good person')