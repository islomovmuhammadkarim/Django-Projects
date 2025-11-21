from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('activate/<uidb64>/<token>/', views.activate_account_view, name='activate'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
]
