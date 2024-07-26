from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,"home.html")

def about(request):
    return render (request, "about.html")

def projects (request):
    return render (request,"projects.html")