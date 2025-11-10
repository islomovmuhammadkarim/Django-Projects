from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/")   # home sahifaga yo'naltirish
    else:
        form = UserCreationForm()
    
    return render(request, "register.html", {'form': form})

def login_view(request):
    if request.method == "POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('/')
        return redirect('login')
    else:
        form=AuthenticationForm()
    return render(request, "login.html", {'form': form})

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("/")
