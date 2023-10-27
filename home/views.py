from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
        if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          contact=Contact(name=name,email=email,phone=phone,date=datetime.today())
          contact.save()
          messages.success(request,"Your contact is submited , we respond you as soon as possible")
        return render(request,'index.html')
    

def portfolio(request):
     return render(request,'portfolio.html')

 
def Addition(num1,num2):
    result = int(num1) + int(num2)
    return f"{num1}+{num2}={result}"
 
def Subtract(num1,num2):
    result = int(num1) - int(num2)
    return f"{num1}-{num2}={result}"
 
def Divide(num1,num2):
    result = int(num1) / int(num2)
    return  f"{num1}/{num2}={result}"
 
def Multiply(num1,num2):
    result = int(num1) * int(num2)
    return  f"{num1}*{num2}={result}"


def calculator(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if 'add' in request.POST:
            result = Addition(num1,num2)
            return render(request,'calculator.html',{'result':result})
        
        if 'sub' in request.POST:
            result = Subtract(num1,num2)
            return render(request,'calculator.html',{'result':result})
 
        if 'div' in request.POST:
            result = Divide(num1,num2)
            return render(request,'calculator.html',{'result':result})
 
        if 'mul' in request.POST:
            result = Multiply(num1,num2)
            return render(request,'calculator.html',{'result':result})
    return render(request,'calculator.html')