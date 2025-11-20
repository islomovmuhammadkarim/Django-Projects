from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .forms import RegistrerForm
from django.http import HttpResponse

# Register
def register_view(request):
    error = None
    if request.method == "POST":
        form = RegistrerForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password1'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    is_active=False
                )
                
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                activate_link = f"http://127.0.0.1:8000/users/activate/{uid}/"


                send_mail(
                    'Activate your account',
                    f'Accountni aktivlashtirish uchun link: {activate_link}',
                    'webmaster@localhost',
                    [form.cleaned_data['email']],
                    fail_silently=False,
                )

                return render(request, 'users/email_sent.html')

            except Exception as e:
                error = f"Xatolik yuz berdi: {str(e)}"
        else:
            # Form xatolari bo'lsa
            error = "Iltimos, barcha maydonlarni to‘g‘ri to‘ldiring."
    else:
        form = RegistrerForm()

    return render(request, 'users/register.html', {'form': form, 'error': error})

# Activate

def activate_view(request, uid):
    try:
        user_id = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=user_id)
        if not user.is_active:
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            # Foydalanuvchi allaqachon aktiv
            error = "Akkountingiz allaqachon faollashtirilgan."
            return render(request, 'users/activate_failed.html', {'error': error})
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        # UID noto‘g‘ri yoki foydalanuvchi topilmadi
        error = "Aktivatsiya linki noto‘g‘ri yoki foydalanuvchi mavjud emas."
        return render(request, 'users/activate_failed.html', {'error': error})
# Login
def login_view(request):
    error_msg = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                # Foydalanuvchi faollashtirilmagan
                error_msg = "Foydalanuvchi faollashtirilmagan. Iltimos, emailingizni tekshiring."
                return render(request, 'users/activate_failed.html', {'error': error_msg})
        else:
            # Username yoki parol noto‘g‘ri
            error_msg = "Username yoki parol noto‘g‘ri."
            return render(request, 'users/activate_failed.html', {'error': error_msg})
    
    return render(request, 'users/login.html')



# Resend activation
def resend_activation_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            if not user.is_active:
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                activate_link = f"http://127.0.0.1:8000/users/activate/{uid}/"
                send_mail(
                    'Activate your account',
                    f'Accountni aktivlashtirish uchun link: {activate_link}',
                    'webmaster@localhost',
                    [email],
                    fail_silently=False,
                )
            return render(request, 'users/email_sent.html', {'email': email})
        except User.DoesNotExist:
            return render(request, 'users/activate_failed.html', {'error': 'Bunday email topilmadi!'})
    return render(request, 'users/resend_activation.html')



def logout_user(request):
    logout(request)
    return redirect('home')     # logoutdan keyin qayerga qaytishi
