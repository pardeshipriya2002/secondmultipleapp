from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def app1(request):
    return HttpResponse("Welcome to app1 page...!!!")
