from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, Textarea, FileInput, EmailInput
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from better_profanity import profanity
from insta.models import PostComment, Post, Story

from .models import CustomUser

user_model = get_user_model()
class CustomUserCreationFormAdmin(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'bio','is_private', 'followed')
class CustomUserCreationForm(forms.Form):
    email = forms.EmailField(label='', widget=EmailInput(attrs= {'placeholder': 'Email', "class":"w-100 borderradius-input-field"}))
    username = forms.CharField(label='', min_length=4, max_length=150, widget=TextInput(attrs={'placeholder': 'username', 'class': "w-100 borderradius-input-field"}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "w-100 borderradius-input-field"}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={"placeholder":"Confirm password", "class":"w-100 borderradius-input-field"}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = user_model.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = user_model.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = user_model.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "last_name", "first_name", "is_private")

class PostCommentCreateForm(ModelForm):
    def clean_description(self):
        data = self.cleaned_data["description"]
        #check if there are no swearwords in comment
        if profanity.contains_profanity(data):
           raise ValidationError(_('Please do not use swear words!'))
        return data

    class Meta:
        model = PostComment
        fields = ["description"]
        labels = {"description":_('') }
        help_texts = {"description":_('')}
        widgets = {
            'description': TextInput(attrs={'placeholder': 'Add comment...', "class": "border-0 d-inline comment-input",}),
        }

class UserUpdateForm(ModelForm):

    def clean_prof_pic(self):
        data = self.cleaned_data["prof_pic"]
        return data

    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        return data

    def clean_username(self):
        data = self.cleaned_data["username"]
        return data

    def clean_bio(self):
        data = self.cleaned_data["bio"]
        return data
    
    def clean_email(self):
        data = self.cleaned_data["email"]
        return data

    def get_user_profpic(self):
        
        return self.request.user.prof_pic.url

    class Meta:
        model = user_model
        fields = ["prof_pic", "first_name", "username", "bio", "email", "is_private"]
        labels = {"prof_pic":_('Profile Picture'), "bio":_('Description'), "username":_("Username"), "first_name":_('Name'), "email":_('E-Mail')}
        help_texts = {"username": _(""), "prof_pic":_("")}
        widgets = {
            'prof_pic': FileInput(attrs={"class": "d-block d-md-inline mb-3 ml-md-2",}),
            'bio': Textarea(attrs={'placeholder': 'Description', "class": "border-update-user-input d-block d-md-inline mb-3 ml-md-2 borderradius-input-field w-100 height-textarea-update-user p-2",}),
            'username': TextInput(attrs={'placeholder': 'Username', "class": "border-update-user-input d-block d-md-inline mb-3 ml-md-2 borderradius-input-field w-100 px-2 height-input-update-user",}),
            'first_name': TextInput(attrs={'placeholder': 'Name', "class": "border-update-user-input d-block d-md-inline mb-3 ml-md-2 borderradius-input-field w-100 px-2 height-input-update-user",}),
            'email': TextInput(attrs={'placeholder': 'E-Mail', "class": "border-update-user-input d-block d-md-inline mb-3 ml-md-2 borderradius-input-field w-100 px-2 height-input-update-user",}),
        }

class StoryCreateForm(ModelForm):
    class Meta:
        model = Story
        fields = ["picture"]
        labels= {"picture":_(""),}
        widgets = {
                "picture": FileInput(attrs={"id":'pictureStory'})
        }
