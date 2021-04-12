from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, Textarea, FileInput
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


from insta.models import PostComment, Post
from .models import CustomUser

user_model = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'bio',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', "last_name", "first_name")



class PostCommentCreateForm(ModelForm):
    def clean_description(self):
        data = self.cleaned_data["description"]
        #check if there are no swearwords in comment
        if "motherfucker" in data or "dick" in data:
           raise ValidationError(_('Please do not use swear words!'))
        a = []
        for x in data:
            if x == '@':
                a.append(x)
        if len(a) != len(set(a)):
           raise ValidationError(_(""))
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
        fields = ["prof_pic", "first_name", "username", "bio", "email"]
        labels = {"prof_pic":_('Profile Picture'), "bio":_('Description'), "username":_("Username"), "first_name":_('Name'), "email":_('E-Mail')}
        help_texts = {"username": _(""), "prof_pic":_("")}
        widgets = {
            'prof_pic': FileInput(attrs={"class": "d-block d-md-inline mb-3 ml-md-2",}),
            'bio': Textarea(attrs={'placeholder': 'Description', "class": "border-update-user-input d-block d-md-inline mb-3 ml-md-2 borderradius-input-field w-100 height-textarea-update-user p-2",}),
            'username': TextInput(attrs={'placeholder': 'Username', "class": "border-update-user-input d-block d-md-inline mb-3 ml-md-2 borderradius-input-field w-100 px-2 height-input-update-user",}),
            'first_name': TextInput(attrs={'placeholder': 'Name', "class": "border-update-user-input d-block d-md-inline mb-3 ml-md-2 borderradius-input-field w-100 px-2 height-input-update-user",}),
            'email': TextInput(attrs={'placeholder': 'E-Mail', "class": "border-update-user-input d-block d-md-inline mb-3 ml-md-2 borderradius-input-field w-100 px-2 height-input-update-user",}),
        }

