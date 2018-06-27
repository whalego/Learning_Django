from django.shortcuts import render
from django.http import HttpResponse

def Web_Page(request):
    return HttpResponse("helloworld")


