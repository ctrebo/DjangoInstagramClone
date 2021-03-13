from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class CustomUser(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)
    prof_pic    = models.ImageField(upload_to ='pp_pics/', height_field=None, width_field=None, default="default_pp.jpg")
    bio         = models.TextField(max_length=150, blank=True, null=True)

class Post(models.Model):
    """
    Model representing a Post
    """

    author = models.ForeignKey(User, on_delete=modles.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    picture = models.ImageField(upload_to="images_post", height_field=400, width_field=400)
    caption = models.TextField(max_length=1500, blank=True, null=True)

    class Meta:
        ordering = [post_date]

    def __str__(self):
        return self.author + " " + caption

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

class BlogComment(models.Model):
    """
    Model representing a comment against a blog post.
    """
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because BlogComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
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