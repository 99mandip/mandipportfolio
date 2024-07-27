from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings 
import os 
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
    experience=[
        {"company":"Writelion Tech",
         "position":"Front-end Developer"}
    ]
    return render (request,"experience.html",{"experience":experience})

def certificate (request):
    return render (request, "certificate.html")

def contact (request):
    return render (request, "contact.html")

def resume (request):
    resume_path=os.path.join(settings.STATIC_ROOT, 'mypdf/resume.pdf')
    if os.path.exists(resume_path):
        with open(resume_path, 'rb') as resume_file:
            response = HttpResponse(resume_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
            return response
    else:
        return HttpResponse("Resume not found", status=404)