from django.shortcuts import render

# Create your views here.


def index(request):
    tasks = ["foo", "baz", "bar"]
    return render(request, "taskapp/index.html", {
        "task": tasks
    })

def add_task_form(request):
    return render(request, "taskapp/add_task_form.html" )
