from django.shortcuts import render
from . models import Skill, Project, Eduaction, Interest
# Create your views here
def home(request):
    resume ={}
    resume['skills']=Skill.objects.all()
    resume['projects'] =Project.objects.order_by('-date_completed')
    # for now im going to keep this unhiglighted
    #resume['education']=Eduaction.objects.all()
    resume['interests'] = Interest.objects.all()
    #job_experience will come later 
    return render(request, 'base/index.html',resume)
     