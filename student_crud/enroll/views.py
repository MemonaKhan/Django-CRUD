from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'enroll/index.html')
    # return render(request, 'tasks/list.html', context)

def add(request):
    return render(request, 'enroll/add.html')

def update(request):
    return render(request, 'enroll/edit.html')


def delete(request):
    return render(request, 'enroll/delete.html')
