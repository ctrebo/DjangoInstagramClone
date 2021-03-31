from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


from insta.models import PostComment, Post
from .models import CustomUser

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