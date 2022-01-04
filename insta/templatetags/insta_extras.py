from django import template
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.template.defaultfilters import stringfilter
from insta.models import Hashtag, Post
from django.http import Http404


register = template.Library()

@register.simple_tag
@stringfilter
def get_tagged_user(tagged_user, logged_in_user):
    if len(tagged_user) > 1: 
        user_model = get_user_model()
        if user_model.objects.filter(username=tagged_user[1:]).count() != 0:
            user = get_object_or_404(user_model, username=tagged_user[1:])
            if(user == logged_in_user):
                return reverse("profpage-user")
            return reverse('user-detail', args=[str(user.id)])
        else:
            #return to custom page
            return reverse('object-dont-exist', args=[str(tagged_user[1:])])
    else:
        return ""

def addPostToHashtag(hashtag, post_id):
    post = get_object_or_404(Post, id=post_id)
    # If post not in hashtag, add post to hashtag
    if (not post.hashtag_posts.filter(id=hashtag.id).exists()):
        hashtag.posts.add(post)


@register.simple_tag
@stringfilter
def get_hashtag_path(word_hashtag, comment_author, post_author, post_id):
    if (len(word_hashtag) > 1): 
        hashtag_exists = Hashtag.objects.filter(hashtag_name=word_hashtag).exists()
        if (comment_author == post_author):
            if hashtag_exists:
                hashtag = Hashtag.objects.get(hashtag_name=word_hashtag)
            else:
                hashtag = Hashtag.objects.create(hashtag_name=word_hashtag)

            addPostToHashtag(hashtag, post_id)
            return reverse('hashtag-detail', args=[str(hashtag.id)])
        else:
            # If comment author not equal post author only return
            # to hashtag detail page
            if hashtag_exists:
                hashtag = get_object_or_404(Hashtag, hashtag_name=word_hashtag)
                return reverse('hashtag-detail', args=[str(hashtag.id)])
            else:
                return reverse('object-dont-exist', args=[str(word_hashtag[1:])])
    else:
        return ""
