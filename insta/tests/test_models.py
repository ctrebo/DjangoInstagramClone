from django.test import TestCase
from ..models import BlogAuthor, BlogComment, Blog
from django.contrib.auth import get_user_model

user_model = get_user_model()