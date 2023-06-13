from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return HttpResponse('Hello')

def home(request):
    return render(request, 'myapp/home.html')