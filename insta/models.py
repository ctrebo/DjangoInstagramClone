import pytz
import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
import datetime
from datetime import timezone, timedelta
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.utils import timezone


from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError


from .validators import validate_file_extension

class CustomUser(AbstractUser):
    date_joined      = models.DateTimeField(auto_now_add=True)
    prof_pic         = models.ImageField(upload_to ='pp_pics/', height_field=None, width_field=None, default="default_pp.jpg")
    bio              = models.TextField(max_length=150, blank=True, null=True)

    # People user is following
    followed         = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_field', blank=True)

    # Hashtags user is following
    followed_hashtags= models.ManyToManyField('Hashtag', related_name='followed_field_hashtag', blank=True)
    saved_posts      = models.ManyToManyField('Post', related_name="saved_post_field", blank=True)
    is_private       = models.BooleanField(default=False)
    # If user is private and someone tries to follow this user
    # request gets added to users account
    pending_requests = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='private_requests', blank=True) 

    @property
    def bio_to_array(self):
        # Add "<new_line_code/>" after every newline. Then rejoin everything.
        # At the end split the text again into words
        return ("".join([s + " <new_line_code/> " for s in self.bio.splitlines()]).split())

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})

class Post(models.Model):
    """
    Model representing a Post
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)
    picture = models.FileField(upload_to="images_post", validators=[validate_file_extension])
    caption = models.TextField(max_length=1500, blank=True, null=True)
    tagged_people = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tagging", blank=True)

    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        return self.author.username + " " + str(self.pk)

    @property
    def caption_to_array(self):
        return ("".join([s + " <new_line_code/> " for s in self.caption.splitlines()]).split())

    def get_absolute_url(self):
        """
        Return url of 'create-comment' because that serves as alternative to a 'post-detail' url. Posts can be watched there. 
        """
        return reverse('create-comment', kwargs={'pk': self.pk})

    @property
    def number_of_likes(self):
        """
        return number of likes on post
        """
        num_likes = self.likes.count()
        if num_likes < 1000:
            return num_likes
        elif num_likes>= 1000 and num_likes< 1000000:
            return str(num_likes//1000)+"k"
        elif num_likes>=1000000 and num_likes < 1000000000:
            return str(num_likes//1000000) + "M"
        else:
             return str(num_likes//1000000000)+"B"
    

    @property
    def time_posted_ago(self):
        """
        Return when difference of now and time, when it was posted
        """
        difference = datetime.datetime.now(timezone.utc) - self.post_date 
        if difference.total_seconds() < 1:
            return "Now"
        elif difference.total_seconds() < 60 and difference.total_seconds() > 1:
            result= str(difference.total_seconds())[:-7]
            if result == "1":
                return result + " second ago"
            else:
                return result + " second ago"                
        elif difference.total_seconds()/60 < 60 and difference.total_seconds()/60 > 1:
            result = str(divmod(difference.total_seconds(), 60)[0])[:-2]
            if result == "1":
                return result + " minute ago"
            else:
                return result + " minutes ago"   
        elif difference.total_seconds()/(60*60) < 24 and difference.total_seconds()/(60*60) >= 1:
            result = str(divmod(difference.total_seconds(), (60*60))[0])[:-2]
            if result == "1":
                return result + " hour ago"
            else:
                return result + " hours ago"  
        elif difference.total_seconds()/(60*60*24) <= 30 and difference.total_seconds()/(60*24*60) >= 1:
            result= str(divmod(difference.total_seconds(), (60*60*24))[0])[:-2]
            if result == "1":
                return result + " day ago"
            else:
                return result + " days ago"  
        elif difference.total_seconds()/(2628002.88) < 12 and difference.total_seconds()/(2628002.88) >= 1:
            result = str(divmod(difference.total_seconds(), 2628002.88)[0])[:-2]
            if result == "1":
                return result + " month ago"
            else:
                return result + " months ago"  
        elif difference.total_seconds()/(31556952) >= 1:
            result = str(divmod(difference.total_seconds(), 31556952)[0])[:-2]
            if result == "1":
                return result + " year ago"
            else:
                return result + " years ago"
        else:
            return "undefined"

    @property
    def is_image(self):
        """
        returns true if Post has image as, not video.
        Used is template to select right html tags
        """
        ext = os.path.splitext(self.picture.url)[1]
        image_extensions = [".jpg", ".png", ".jpeg"]
        return (ext in image_extensions)

def tagged_people_changed(sender, **kwargs):
    if kwargs['instance'].tagged_people.count() > 20:
        raise ValidationError("You can't tag more than 20 people")  
m2m_changed.connect(tagged_people_changed, sender=Post.tagged_people.through)    

class PostComment(models.Model):
    """
    Model representing a comment against a blog post.
    """
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # Foreign Key used because BlogComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_field', blank=True)
    parent = models.ForeignKey("PostComment", related_name="replies", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring


    @property
    def description_to_array(self):
        # Add "<new_line_code/>" after every newline. Then rejoin everything.
        # At the end split the text again into words
        return ("".join([s + " <new_line_code/> " for s in self.description.splitlines()]).split())

    @property
    def time_commented_ago(self):
        """
        Function that return how long ago post was created
        """

        difference = datetime.datetime.now(timezone.utc) - self.post_date 
        if difference.total_seconds() < 1:
            return "Now"
        elif difference.total_seconds() < 60 and difference.total_seconds() > 1:
            result= str(difference.total_seconds())[:-7]
            if result == "1":
                return result + " second ago"
            else:
                return result + " second ago"                
        elif difference.total_seconds()/60 < 60 and difference.total_seconds()/60 > 1:
            result = str(divmod(difference.total_seconds(), 60)[0])[:-2]
            if result == "1":
                return result + " minute ago"
            else:
                return result + " minutes ago"   
        elif difference.total_seconds()/(60*60) < 24 and difference.total_seconds()/(60*60) >= 1:
            result = str(divmod(difference.total_seconds(), (60*60))[0])[:-2]
            if result == "1":
                return result + " hour ago"
            else:
                return result + " hours ago"  
        elif difference.total_seconds()/(60*60*24) <= 30 and difference.total_seconds()/(60*24*60) >= 1:
            result= str(divmod(difference.total_seconds(), (60*60*24))[0])[:-2]
            if result == "1":
                return result + " day ago"
            else:
                return result + " days ago"  
        elif difference.total_seconds()/(2628002.88) < 12 and difference.total_seconds()/(2628002.88) >= 1:
            result = str(divmod(difference.total_seconds(), 2628002.88)[0])[:-2]
            if result == "1":
                return result + " month ago"
            else:
                return result + " months ago"  
        elif difference.total_seconds()/(31556952) >= 1:
            result = str(divmod(difference.total_seconds(), 31556952)[0])[:-2]
            if result == "1":
                return result + " year ago"
            else:
                return result + " years ago"   


class StoryManager(models.Manager):
    def get_queryset(self):
        """
        return only stories that have been created in less than 24h
        """
        return super(StoryManager, self).get_queryset().filter(created_at__gt=(timezone.now()-datetime.timedelta(days=1)))

class Story(models.Model):
    """
    Stories should only be visible for 24h
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to="images_stories", height_field=None, width_field=None)
    # When using Story.active_story_objects.all() now the queryset
    # of StoryManager gets used
    objects = StoryManager()

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.author.username + " " + str(self.pk)


    @property
    def time_posted_ago(self):
        """
        Function that return how long ago post was created
        """

        difference = datetime.datetime.now(timezone.utc) - self.created_at 
        if difference.total_seconds() < 1:
            return "Now"
        elif difference.total_seconds() < 60 and difference.total_seconds() > 1:
            result= str(difference.total_seconds())[:-7]
            if result == "1":
                return result + " s"
            else:
                return result + " s"                
        elif difference.total_seconds()/60 < 60 and difference.total_seconds()/60 > 1:
            result = str(divmod(difference.total_seconds(), 60)[0])[:-2]
            if result == "1":
                return result + " m"
            else:
                return result + " m"   
        elif difference.total_seconds()/(60*60) < 24 and difference.total_seconds()/(60*60) >= 1:
            result = str(divmod(difference.total_seconds(), (60*60))[0])[:-2]
            if result == "1":
                return result + " h"
            else:
                return result + " h"  

class Hashtag(models.Model):
    hashtag_name = models.CharField(max_length=50, unique=True)
    posts = models.ManyToManyField(Post, related_name='hashtag_posts', blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.hashtag_name
    
    def get_absolute_url(self):
        return reverse('hashtag-detail', kwargs={'pk': self.pk})
