from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -.> response

def say_world(request):
    return render(request, 'hello.html')
    # Pull data from db
    #Transform
    #send emails

def world():
    return HttpResponse('Hello World')
