
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request,'polls/index.html', context )#HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return  render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)

def testView(request, testId):
    context = {'testId':testId, 'lst':[1,2,3,4,5]}
    return render(request, 'polls/test.html', context)