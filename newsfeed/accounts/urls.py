from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from . import views

urlpatterns = [

    path('profile/<str:username>/', views.profile, name='user_profile'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('profile-redirect/', views.profile_redirect, name='profile_redirect'),
    #Sign up
    path('signup/', views.user_register, name='signup'),
    # Login
    path('login/', LoginView.as_view(
        template_name='accounts/login.html',
        redirect_authenticated_user=True
    ), name='login'),

    # Logout (POST bilan ishlash uchun next_page yoki template)
    path('logout/', LogoutView.as_view(
        template_name='accounts/logout.html',
        next_page='login'  # Logoutdan keyin login sahifaga yo‘naltiradi
    ), name='logout'),

    # Password Reset (parolni tiklash)
    path('password_reset/', PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        email_template_name='accounts/password_reset_email.html',
        subject_template_name='accounts/password_reset_subject.txt',
        success_url='/accounts/password_reset/done/'
    ), name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url='/accounts/reset/done/'
    ), name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]
