from django.http import HttpResponse
# Create your views here.

# Create your views here.
from django.shortcuts import render



def home(request):
    return HttpResponse('Hello,Django World!')


def about(request):
    return HttpResponse('This is the about page.')


def contact(request):
    return HttpResponse('This is the contact page.')



def dashboard(request):
    return render(request, 'dashboard.html')