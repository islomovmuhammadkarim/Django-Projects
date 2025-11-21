from django.shortcuts import render, redirect
from .models import Todo,TimeCategory
from django.db.models import Case, When, IntegerField
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required
def dashboard_view(request):
    user = request.user
    todos = Todo.objects.filter(user=user).annotate(
        priority_order=Case(
            When(priority='high', then=1),
            When(priority='medium', then=2),
            When(priority='low', then=3),
            output_field=IntegerField(),
        )
    ).order_by('completed', 'priority_order')

    # Dashboard Stats
    total_tasks = todos.count()
    completed_tasks = todos.filter(completed=True).count()
    in_progress_tasks = todos.filter(completed=False).count()

    # HomeTime uchun jami vaqt
    total_minutes = TimeCategory.objects.filter(user=user).aggregate(total=Sum('total_minutes'))['total'] or 0
    total_time = f"{total_minutes // 60} soat {total_minutes % 60} min"

    context = {
        'todos': todos,
        'dashboard_stats': {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'in_progress_tasks': in_progress_tasks,
            'total_time': total_time
        }
    }

    return render(request, 'todo/dashboard.html', context)


from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todo

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority', 'medium')  # default priority

        if title:
            # Foydalanuvchini bog‘laymiz
            Todo.objects.create(user=request.user, title=title, priority=priority)

    return redirect('dashboard')


@login_required
def toggle_todo(request, todo_id):
    # Faqat shu foydalanuvchining todo’sini olish
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('dashboard')


@login_required
def delete_todo(request, todo_id):
    # Faqat shu foydalanuvchining todo’sini o‘chirish
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('dashboard')


@login_required
def hometimer_view(request):
    user = request.user

    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        minutes = request.POST.get('minutes')

        # Qo'shish
        if 'add_time' in request.POST and category_id and minutes:
            category = TimeCategory.objects.get(id=category_id, user=user)
            category.total_minutes += int(minutes)
            category.save()

        # Ayirish
        elif 'subtract_time' in request.POST and category_id and minutes:
            category = TimeCategory.objects.get(id=category_id, user=user)
            category.total_minutes = max(0, category.total_minutes - int(minutes))
            category.save()

        # O'chirish
        elif 'delete_category' in request.POST and category_id:
            category = TimeCategory.objects.get(id=category_id, user=user)
            category.delete()

        # Yangi soha qo'shish
        elif 'category_name' in request.POST:
            name = request.POST.get('category_name')
            if name:
                TimeCategory.objects.get_or_create(user=user, name=name)

        return redirect('hometimer')

    # GET so'rov
    categories = TimeCategory.objects.filter(user=user)
    # Har bir category uchun soat va minut hisoblash
    for cat in categories:
        cat.hours = cat.total_minutes // 60
        cat.minutes = cat.total_minutes % 60

    return render(request, 'todo/hometimer.html', {'categories': categories})


@login_required
def get_time_categories(request):
    categories = TimeCategory.objects.filter(user=request.user)

    data = []
    for cat in categories:
        total = cat.total_minutes
        data.append({
            "id": cat.id,
            "name": cat.name,
            "total_minutes": total,
        })

    return JsonResponse({"categories": data})



@login_required
def important_tasks_api(request):
    tasks = Todo.objects.filter(user=request.user, priority='high', completed=False)
    
    data = [
        {"title": t.title, "priority": t.priority, "completed": t.completed}
        for t in tasks
    ]
    
    return JsonResponse({"tasks": data})
