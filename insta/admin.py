from django.contrib import admin
from .models import CustomUser, PostComment, Post, Story, Hashtag
from .forms import CustomUserCreationForm, CustomUserCreationFormAdmin, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationFormAdmin
    form = CustomUserChangeForm
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_private', 'id')
    list_filter = ('date_joined', 'username')

    fieldsets = (
        (None, {
            'fields': ('username', "password")}),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'last_login',)}),
        ('Permissions',{
            'fields': ('is_private', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),

        ('Custom user', {'fields': ('bio', 'prof_pic', 'followed', 'saved_posts', 'pending_requests', )}),
    )
   
   #variables that will be displayed on the creaet user side
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1','password2', 'bio', 'is_staff', 'is_active', 'is_private')}
        ),
    )

class PostCommentInline(admin.TabularInline):
    model = PostComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "post_date", "id")
    list_filter = ("author", "post_date")

    # readonly_fields = ('id',)


    fieldsets = (("Post information", {'fields': ('author', 'likes', 'picture', 'caption', 'tagged_people')}),)

    inlines = [PostCommentInline]

@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post_date", "description", "id", "post",)
    list_filter = ("author", "post_date", "post")

    fieldsets = (("Post Comment information", {'fields': ('author', 'description', 'post', 'likes', 'parent')}),)

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("author", "created_at", "id")
    list_filter = ("author", "created_at")


    fieldsets = (("Story information", {'fields': ('author', 'picture')}),)

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ("hashtag_name", "id")
    list_filter = ("hashtag_name",)

    fieldsets = (("Hashtag information", {"fields": ("hashtag_name",)}),)
