from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def wish2(request):
    s="<h1> welcome i am from secondapp</h1>"
    return HttpResponse(s)