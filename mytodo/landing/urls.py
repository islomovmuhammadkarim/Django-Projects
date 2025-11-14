from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # ToDo CRUD
    path('todos/', views.todo_list, name='todo_list'),
    path('todo/<int:todo_id>/delete/', views.todo_delete, name='todo_delete'),
    path('todo/<int:todo_id>/edit/', views.todo_edit, name='todo_edit'),
]
