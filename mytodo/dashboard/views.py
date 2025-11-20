from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user).order_by('-is_important', '-created_at')

    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Todo.objects.create(user=request.user, title=title)
        return redirect('todo_list')

    return render(request, 'todo_list.html', {'todos': todos})

@login_required
def toggle_complete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('todo_list')

@login_required
def toggle_important(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.is_important = not todo.is_important
    todo.save()
    return redirect('todo_list')

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('todo_list')
