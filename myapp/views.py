from django.shortcuts import render,redirect
from .models import *


def home(request):
    task_c=Task.objects.filter(status="completed")
    task_p=Task.objects.filter(status="pending").order_by('-id')

    vars = {
        "task_c":task_c,
        "task_p":task_p
    }

    return render(request, 'home.html', vars)

def task_create(request):
    if request.method=="POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')

        task = Task(
            name = name,
            desc = desc,
            status = "pending",
        )

        task.save()
        return redirect("/")


    return render(request, 'task_create.html')

def task_update(request, pk):
    task= Task.objects.get(id=pk)
    task.status="completed"
    task.save()
    return redirect("/")



