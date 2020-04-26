from django.shortcuts import render

from . import models
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todo_app.models import Todo
from django.http import HttpResponseRedirect
def home(request):
    todo_items=Todo.objects.all().order_by("-added_date")
    return render(request,'main/index.html',{
        "todo_items":todo_items
        })


# Create your views here.
@csrf_exempt
def add_todo(request):
    
    current_date=timezone.now()
    content=request.POST["content"]
    created_object=Todo.objects.create(added_date=current_date,text=content)
   
    length_of_todos=Todo.objects.all().count()
    
    return HttpResponseRedirect('/')
@csrf_exempt
def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    
    return HttpResponseRedirect('/')
@csrf_exempt
def update_todo(request,todo_id):
    HttpResponseRedirect('main/edit.html')
    doid=Todo.objects.get(id=todo_id)
    
    return render(request,'main/index.html')
    