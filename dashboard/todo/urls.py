# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),         # Dashboard asosiy sahifa   
    path('add/', views.add_todo, name='add_todo'),            # Yangi vazifa qo'shish
    path('toggle/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('hometimer/', views.hometimer_view, name='hometimer'),
    path('api/time-categories/', views.get_time_categories, name='time-categories'),
    path('api/important-tasks/', views.important_tasks_api, name='api_important_tasks'),
    
    ]