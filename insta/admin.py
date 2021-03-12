from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username', 'first_name', 'last_name', "email", )
    list_filter = ('date_joined', 'username')

    fieldsets = (
        (None, {
            'fields': ('username', "password")}),
        # ('Personal Information', {
            # 'fields': ('email', 'last_name', "first_name")}),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'last_login',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),

        ('Custom user', {'fields': ('bio', 'prof_pic',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )



