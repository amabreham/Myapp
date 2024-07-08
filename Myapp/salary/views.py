from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request,'Home.html')

def addemployee(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phonenumber = request.POST.get('phonenumber')
        gender = request.POST.get('gender')
        salary = request.POST.get('salary')
        
        Employee.objects.create(first_name=firstname, last_name=lastname, phone_number=phonenumber,gender=gender, salary=salary).save()
    employee = Employee.objects.all()
    context = {'employee': employee}
    return render(request,'addemployee.html', context)