from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this

from .models import Post, PostComment

from insta.forms import PostCommentCreateForm, UserUpdateForm

User = settings.AUTH_USER_MODEL

class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.exclude(author=self.request.user).order_by("-post_date")
    
    def get_context_data(self, **kwargs):
        user_model = get_user_model()
        users = user_model.objects.all().exclude(username=self.request.user.username)

        liked = []
        for post in Post.objects.exclude(author=self.request.user).order_by("-post_date"):
            if post.likes.filter(id=self.request.user.id).exists():
                liked.append(" text-danger")
            else:
                liked.append(" text-white fontawesome-border")

        context = super(PostListView, self).get_context_data(**kwargs)
        context["list_liked"] = liked
        context["recommandation_list"] = users
        return context


def blogPostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('create-comment', args=[str(pk)]))

@csrf_exempt
def blogPostLikeListView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('index'))

@login_required
def postCommentCreate(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    
    post_for_comment = get_object_or_404(Post, pk=pk)
    other_posts_of_author = post_for_comment.author.post_set.all().exclude(pk=post_for_comment.pk)[:6]
    comment_list = PostComment.objects.filter(post=post_for_comment).order_by("post_date")

    likes_connected = get_object_or_404(Post, id=pk)
    liked = False
    if likes_connected.likes.filter(id=request.user.id).exists():
        liked = True

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
        'other_posts_of_author': other_posts_of_author,
        'number_of_likes': likes_connected.number_of_likes(),
        'post_is_liked': liked, 
    }

    return render(request, 'insta/postcomment_form.html', context)


@login_required
def updateUser(request, pk):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        # Check if the form is valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('profpage-user') )
    # If this is a GET (or any other method) create the default form.
    else:
        form = UserUpdateForm(instance=request.user)
        

    context = {
        'form': form,

    }
    return render(request, 'insta/user_update_form.html', context)



def user_detail(request, pk):
    user_model = get_user_model()
    user_for_page = get_object_or_404(user_model, pk=pk)

    context = {
        'user_for_page': user_for_page, 
    }

    return render(request, 'insta/user_detail.html', context)

class ProfilPageListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "insta/profil_page_by_user.html"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["picture", "caption"]

    def get_success_url(self):
        """
        After posting comment return to blog page
        """
        return reverse("profpage-user")


    def form_valid(self, form):
        """
        Add author form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of post
        form.instance.author = self.request.user
        # Call super-class form validation behaviour
        return super(PostCreateView, self).form_valid(form)

