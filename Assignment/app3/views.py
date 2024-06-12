from django.shortcuts import render
from django.http import HttpResponse


def factorial(n):             
    pr=1
    for i in range(2,n+1):
        pr=pr*i
    return pr

def listfactorials(request):
    n=8
    d={}
    for i in range(1,n+1):
        d[i]=factorial(i)
    
    return render(request,'app3/index.html',{'factorials':d})
