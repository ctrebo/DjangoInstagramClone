from django import template
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.simple_tag
@stringfilter
def get_tagged_user(tagged_user, self_user):
    if len(tagged_user) > 1: 
        user_model = get_user_model()
        if user_model.objects.filter(username=tagged_user[1:]).count() != 0:
            user = get_object_or_404(user_model, username=tagged_user[1:])
            if(user == self_user):
                return reverse("profpage-user")
            return reverse('user-detail', args=[str(user.id)])
        else:
            #return to custom page
            return reverse('user-dont-exist', args=[str(tagged_user[1:])])
    else:
        return ""