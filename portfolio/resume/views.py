from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,"home.html")

def about(request):
    return render (request, "about.html")

def projects (request):
    projects_show=[
        { 
            'title':'Personal Portfolio',
            'path':'images/portfolio.png',
        },
    ]
    return render (request,"projects.html",{"projects_show": projects_show})

def experience(request):
    return render (request, "experience.html")