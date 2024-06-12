from django.shortcuts import render
from django.http import HttpResponse

def func(request):
    n1=5
    square=25
    fact=120
    return render(request,'app1/index.html',{"param1":square,"param2":fact})