from django.contrib import admin

from django.contrib import admin
from .models import CustomUser, PostComment, Post
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
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'last_login',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),

        ('Custom user', {'fields': ('bio', 'prof_pic', 'followed', 'saved_posts')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

class PostCommentInline(admin.TabularInline):
    model = PostComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "post_date", "id")
    list_filter = ("author", "post_date")

    # readonly_fields = ('id',)


    fieldsets = (("Post information", {'fields': ('author', 'likes', 'picture', "caption", "tagged_people")}),)

    inlines = [PostCommentInline]

@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post_date", "description", "id")
    list_filter = ("author", "post_date", "post")

    fieldsets = (("Post Comment information", {'fields': ('author', 'description', "post")}),)

