from django.shortcuts import render

# Create your views here.
def shiv(request):
    return render(request,'shiv.html')

def mahadev(request):
    return render(request,'mahadev.html')
