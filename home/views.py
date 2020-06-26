from django.shortcuts import render
from home.models import Task

# Create your views here.
def home(request):
    context = {
        'success' :False
    }
    # handle the request of form
    if(request.method=='POST'):
        task = request.POST['task']
        desc = request.POST['desc']
        ins = Task(taskName = task, taskDescription = desc)
        ins.save()
        context = {
        'success' :True    }
    return render(request, 'index.html', context)

def tasks(request):
    # fetch all task from task
    allTasks = Task.objects.all()
    context = {
        "tasks" : allTasks
    }
    return render(request, 'tasks.html', context)