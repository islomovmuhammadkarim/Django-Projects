from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/<int:todo_id>/toggle_complete/', views.toggle_complete, name='toggle_complete'),
    path('todos/<int:todo_id>/toggle_important/', views.toggle_important, name='toggle_important'),
    path('todos/<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
]
