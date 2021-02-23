from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentReg

# Create your views here.


def index(request):
    return render(request, 'enroll/index.html')
    # return render(request, 'tasks/list.html', context)

def add(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
    else:
        fm = StudentReg()
    
    return render(request, 'enroll/add.html', {'form':fm})

def update(request):
    return render(request, 'enroll/edit.html')


def delete(request):
    return render(request, 'enroll/delete.html')
