from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegistrationForm, LoginForm, CustomPasswordResetForm, CustomSetPasswordForm

# ===== Registration =====
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Email activation link
            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = f"http://{current_site.domain}/accounts/activate/{uid}/{token}/"

            # Dev: console orqali
            print(f"Activate your account: {activation_link}")
            # send_mail can be added later

            return HttpResponse("Ro'yxatdan o'tdingiz! Emaildagi link orqali hisobingizni aktivatsiya qiling. (Console-ga link chiqarildi)")
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})

# ===== Activation =====
def activate_account_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse("Hisobingiz aktivlashtirildi! Endi login qilishingiz mumkin.")
    else:
        return HttpResponse("Aktivatsiya linki noto'g'ri yoki muddati tugagan.")

# ===== Login =====
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, "Email yoki parol noto‘g‘ri")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

# ===== Logout =====
def logout_view(request):
    logout(request)
    return redirect('login')

# ===== Password Reset =====
def password_reset_request(request):
    if request.method == "POST":
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return HttpResponse("Email topilmadi")

            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = f"http://{current_site.domain}/accounts/reset/{uid}/{token}/"

            print(f"Password reset link: {reset_link}")

            return HttpResponse("Password reset link console-ga yuborildi")
    else:
        form = CustomPasswordResetForm()
    return render(request, "accounts/password_reset.html", {"form": form})

# ===== Password Reset Confirm =====
def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        user = None

    if user is None or not default_token_generator.check_token(user, token):
        return HttpResponse("Link noto'g'ri yoki muddati tugagan")

    if request.method == "POST":
        form = CustomSetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Parolingiz yangilandi! Endi login qilishingiz mumkin.")
    else:
        form = CustomSetPasswordForm(user)
    return render(request, "accounts/password_reset_confirm.html", {"form": form})
