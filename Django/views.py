from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime, timedelta
from .models import Todo
def Django(request):
    if request.method == 'POST':
        todo_txt = request.POST.get('todo')
        
        Todo.objects.create(
            todo = todo_txt,
            completed = 0
        )
        print(todo_txt)
        return redirect('Django:Django')

    todos = Todo.objects.all()
    return render(request, 'Django/django.html',{'todo': todos})
  


def edit(request,id):
    todo = Todo.objects.get(todo_id=id) 
    print(todo.completed)
    if todo.completed == 1 :
        todo.completed = 0
    else :
        todo.completed = 1
    todo.save()        
    print(todo.completed)
    return redirect('Django:Django')

def delete(request, id):   
    todo = Todo.objects.get(todo_id=id)  
    todo.delete()

    return redirect('Django:Django')