from django.shortcuts import render
from django.http import HttpResponse
from demo_celery.celery import add

# Create your views here.

def home(request):
    print("Hi")
    result1 = add.delay(10,20)
    print(result1)
    return HttpResponse("hello world")