from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app2(request):
    return HttpResponse("welcome to app2 page...!!!")