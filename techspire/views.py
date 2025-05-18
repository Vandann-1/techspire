from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render (request,"home.html")

def projectsho(request):
    return render (request,"projects.html")

def founders(request):
    return render (request,"founder.html")