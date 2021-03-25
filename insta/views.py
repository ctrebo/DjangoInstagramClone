from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Post, PostComment

from insta.forms import PostCommentCreateForm
from django.contrib.auth import get_user_model



User = settings.AUTH_USER_MODEL
# Create your views here.

# def BlogPostLike(request, pk):
#     post = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#     else:
#         post.likes.add(request.user)

#     return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))

class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.exclude(author=self.request.user).order_by("-post_date")
    
    def get_context_data(self, **kwargs):
        user_model = get_user_model()
        users = user_model.objects.exclude(username=self.request.user.username)[:5]

        context = super(PostListView, self).get_context_data(**kwargs)
        context["recommandation_list"] = users
        return context



@login_required
def postCommentCreate(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    post_for_comment = get_object_or_404(Post, pk=pk)
    comment_list = PostComment.objects.filter(post=post_for_comment).order_by("post_date")

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = PostCommentCreateForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            #create new object with data from form
            comment=PostComment.objects.create(description=form.cleaned_data["description"], author=request.user, post=post_for_comment)

            comment.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('index') )

    # If this is a GET (or any other method) create the default form.
    else:
        comment = ""
        form = PostCommentCreateForm(initial={"description":comment})

    context = {
        'form': form,
        'post': post_for_comment,
        'comment_list': comment_list, 
    }

    return render(request, 'insta/postcomment_form.html', context)

# class UserDetailView(LoginRequiredMixin, generic.DetailView):
    # model = User
    # context_object_name = 'user_object'

def user_detail(request, pk):
    user_model = get_user_model()
    user_for_page = get_object_or_404(user_model, pk=pk)

    context = {
        'user_for_page': user_for_page, 
    }

    return render(request, 'insta/user_detail.html', context)