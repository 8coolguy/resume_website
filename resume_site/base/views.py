from django.shortcuts import render
from . models import Skill, Project, Eduaction, Interest
# Create your views here
def home(request):
    resume ={}
    #resume['skills']=Skill.objects
    return render(request, 'base/index.html')
     