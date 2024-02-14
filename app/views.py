from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def create_student(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SDFO=StudentForm(request.POST)
        if SDFO.is_valid():
            SDFO.save()
            return HttpResponse('student table is created')
        else:
            return HttpResponse('invalid data')
    
    return render(request,'create_student.html',d)