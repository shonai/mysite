from django.shortcuts import render
from django.http import HttpResponse

from .models import Task
# Create your views here.

def index(request):
    taskList = Task.objects.all().order_by("deadLineDate")
    context = {
        "taskList" : taskList
    }
    return render(request, 'todolist/index.html',context)