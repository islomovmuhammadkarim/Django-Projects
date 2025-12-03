from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, UserEditForm, ProfileEditForm
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from .models import Profile
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('login')
    else:
        user_form = SignUpForm()
    return render(request, 'accounts/signup.html', {'user_form': user_form})


@login_required
def edit_user(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_profile', username=request.user.username)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/profile_edit.html', context)

def profile(request, username):
    user_obj = get_object_or_404(User, username=username)
    profile_obj = user_obj.profile  # OneToOneField orqali Profile
    profile_url = request.build_absolute_uri()
    context = {
        'user_obj': user_obj,
        'profile_obj': profile_obj,
        'profile_url': profile_url
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def profile_redirect(request):
    if request.user.is_authenticated:
        return redirect('user_profile', username=request.user.username)
    return redirect('login')
