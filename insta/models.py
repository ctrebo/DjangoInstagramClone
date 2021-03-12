from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class CustomUser(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)
    prof_pic    = models.ImageField(upload_to ='pp_pics/', height_field=None, width_field=None, default="default_pp.jpg")
    bio         = models.TextField(max_length=150, blank=True, null=True)
