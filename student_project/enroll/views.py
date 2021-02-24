from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .forms import StudentReg
from .models import Student

# Create your views here.


def index(request):
    stud = Student.objects.all()
    return render(request, 'enroll/index.html',{'data':stud})
    # return render(request, 'tasks/list.html', context)
 
def add(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name=nm,email=em,password=pw)
            reg.save()
            
            stud = Student.objects.all()
            return HttpResponseRedirect('/')

            # return render(request, 'enroll/index.html',{'data':stud})


            # fm.save()            # also easy and better way for saving all data in database
        # fm = StudentReg()          # here we do some logic to alert user about data is added or not



    else:
        fm = StudentReg()
    
    return render(request, 'enroll/add.html', {'form':fm})

def update(request,id):
    if request.method == 'POST':
        std = Student.objects.get(pk=id)
        fm = StudentReg(request.POST, instance=std)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
        
    else:
        std = Student.objects.get(pk=id)
        fm = StudentReg(instance=std)
    return render(request, 'enroll/edit.html',{'form':fm})



def delete(request,id):
    # if request.method == 'POST':         # use when button from form
        std = Student.objects.get(pk=id)
        std.delete()
        return HttpResponseRedirect('/')
    # return render(request, 'enroll/index.html')
    # return render(request, 'enroll/delete.html')
