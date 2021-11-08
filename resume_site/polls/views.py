from django.shortcuts import render,get_object_or_404

from .models import Question

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    #his was with out the templates 
    #output =",".join(q.question_str for q in latest_question_list)
    context ={'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html',context)
#this is all for the poll info 
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You are looking at the respone of question %s"
    return HttpResponse(response %question_id)
def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)

