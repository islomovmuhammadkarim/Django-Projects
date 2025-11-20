from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('activate/<uid>/', views.activate_view, name='activate'),
    path('resend/', views.resend_activation_view, name='resend_activation'),
    path('logout/', views.logout_user, name='logout'),
]
