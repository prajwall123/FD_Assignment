from django.shortcuts import render
from django.http import HttpResponse
from app2.forms import inputform1


def sqfct(request):                
    if request.method=="POST":
        form1=inputform1(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get('n1')
            result=factorial(n1)
            return render(request,'app2/index.html',{'n':n1,'sqr':n1**2,'fct':result,'form':form1})
    else:
        form1=inputform1()
        
    return render(request ,'app2/index.html',{'form':form1})

def factorial(n):             
    pr=1
    for i in range(2,n+1):
        pr=pr*i
    return pr
