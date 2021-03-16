from django.shortcuts import render
from django.conf import settings
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import Http404

from .models import Post, PostComment

User = settings.AUTH_USER_MODEL
# Create your views here.

class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.exclude(author=self.request.user).order_by("-post_date")
    

    # def get_context_data(self, **kwargs):
    #     """
    #     Add BlogAuthor to context so they can be displayed in the template
    #     """
    #     # Call the base implementation first to get a context
    #     # context = super(PostListView, self).get_context_data(**kwargs)
    #     context['num_comments'] = PostComment.objects.filter(id=) 
    #     return context




