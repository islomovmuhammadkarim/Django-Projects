from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import About, Todo
from .forms import ContactMessageForm, TodoForm
from datetime import date, timedelta

# Home view: ToDo + Homework
@login_required(login_url='login')
def home(request):
    todos = Todo.objects.filter(user=request.user).order_by('deadline')
    todo_form = TodoForm()

    if request.method == 'POST' and 'add_todo' in request.POST:
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            new_todo = todo_form.save(commit=False)
            new_todo.user = request.user
            if not new_todo.deadline:
                new_todo.deadline = date.today() + timedelta(days=10)
            new_todo.save()
            return redirect('home')

    for todo in todos:
        days = todo.days_left()
        if days is not None:
            if days <= 1:
                todo.color_class = 'deadline-red'
            elif days == 2:
                todo.color_class = 'deadline-orange'
            elif days == 3:
                todo.color_class = 'deadline-green'
            else:
                todo.color_class = 'deadline-black'
        else:
            todo.color_class = 'deadline-black'

    return render(request, 'home.html', {'todos': todos, 'todo_form': todo_form})



@login_required(login_url='login')
def todo_list(request):
    # Foydalanuvchining barcha ToDo’lari deadline bo‘yicha tartiblangan
    todos = Todo.objects.filter(user=request.user).order_by('deadline')
    
    # Rang berish: deadline asosida
    for todo in todos:
        days = todo.days_left() if todo.deadline else None
        if days is not None:
            if days <= 1:
                todo.color_class = 'deadline-red'
            elif days == 2:
                todo.color_class = 'deadline-orange'
            elif days == 3:
                todo.color_class = 'deadline-green'
            else:
                todo.color_class = 'deadline-black'
        else:
            todo.color_class = 'deadline-black'

    return render(request, 'todo/todo_list.html', {'todos': todos})


# ToDo edit
@login_required(login_url='login')
def todo_edit(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {'form': form, 'todo': todo})


# ToDo delete
@login_required(login_url='login')
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('todo_list')













def about(request):
    about = About.objects.first()
    return render(request, 'about.html', {'about': about})


# Contact
def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})


