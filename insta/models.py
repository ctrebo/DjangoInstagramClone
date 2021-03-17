from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
import datetime
from datetime import timezone, timedelta

class CustomUser(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)
    prof_pic    = models.ImageField(upload_to ='pp_pics/', height_field=None, width_field=None, default="default_pp.jpg")
    bio         = models.TextField(max_length=150, blank=True, null=True)

class Post(models.Model):
    """
    Model representing a Post
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='blogpost_like', blank=True)
    picture = models.ImageField(upload_to="images_post", height_field=None, width_field=None)
    caption = models.TextField(max_length=1500, blank=True, null=True)

    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        return self.author.username

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog-author instance.
        """
        return reverse('post-detail', args=[str(self.id)])

    def number_of_likes(self):
        """
        return number of likes on post
        """
        return self.likes.count()
    
    @property
    def time_posted_ago(self):
        """
        Function that return how long ago post was created
        """

        difference = datetime.datetime.now(timezone.utc) - self.post_date 
        if difference.total_seconds() < 60 and difference.total_seconds() > 1:
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

class PostComment(models.Model):
    """
    Model representing a comment against a blog post.
    """
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because BlogComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["-post_date"]

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