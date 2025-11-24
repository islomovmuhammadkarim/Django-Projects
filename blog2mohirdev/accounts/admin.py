from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model=CustomUser
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    list_display=('username','first_name','last_name','email','age','address','is_staff')
    fieldsets = (
        (None, {
            "fields": (
                ('username','first_name','last_name','email','age','address','is_staff')
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            "fields": (
                ('username','first_name','last_name','email','age','address','is_staff')
            ),
        }),
    )
    

admin.site.register(CustomUser,CustomUserAdmin)
