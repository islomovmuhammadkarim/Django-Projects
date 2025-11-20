from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo,TimeCategory
from django.db.models import Case, When, IntegerField

def dashboard_view(request):
    todos = Todo.objects.annotate(
        priority_order=Case(
            When(priority='high', then=1),
            When(priority='medium', then=2),
            When(priority='low', then=3),
            output_field=IntegerField(),
        )
    ).order_by('completed', 'priority_order')  # completed False birinchi, keyin True; priority bo‘yicha sort

    return render(request, 'todo/dashboard.html', {'todos': todos})



def mytodo_view(request):
    # Annotate orqali priority uchun numeric order beramiz
    todos = Todo.objects.annotate(
        priority_order=Case(
            When(priority='high', then=1),
            When(priority='medium', then=2),
            When(priority='low', then=3),
            output_field=IntegerField(),
        )
    ).order_by('completed', 'priority_order')  # completed False birinchi, keyin True; priority bo‘yicha sort

    return render(request, 'todo/mytodo.html', {'todos': todos})



def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority')

        if title and priority:
            Todo.objects.create(title=title, priority=priority)
    return redirect('dashboard')

def toggle_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('mytodo')


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('mytodo')



def stats_view(request):
    todos = Todo.objects.all()
    total = todos.count()
    completed_count = todos.filter(completed=True).count()
    incomplete_count = todos.filter(completed=False).count()

    priority_counts = {
        'high': todos.filter(priority='high').count(),
        'medium': todos.filter(priority='medium').count(),
        'low': todos.filter(priority='low').count(),
    }

    context = {
        'total': total,
        'completed_count': completed_count,
        'incomplete_count': incomplete_count,
        'priority_counts': priority_counts,
    }

    return render(request, 'todo/stats.html', context)





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
