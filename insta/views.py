from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this
from django.db.models import Q # new

#libraries for signup
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


from .models import Post, PostComment

from insta.forms import PostCommentCreateForm, UserUpdateForm, CustomUserCreationForm

user_model = get_user_model()


#signup view
def signup(request):
    """
    view that signes user up and creates a BlogAuthor object for the user
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('index')

    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

class PostListView(LoginRequiredMixin, generic.ListView):
    model = user_model
    template_name = "insta/post_list.html"

    def get_queryset(self):
        ids_followed = self.request.user.followed.all()
        return Post.objects.filter(author__in=ids_followed)

    
    def get_context_data(self, **kwargs):
        
        #get list of id's of users that signed in user follows
        user_vars_values = self.request.user.followed.all().values_list("id")

        #exclude signed in user, people that user follows and people he send a follow request from recommandation list 
        recommandation_list = user_model.objects.all().exclude(username=self.request.user.username).exclude(id__in=user_vars_values).exclude(id__in=self.request.user.private_requests.all())[:7]

        context = super(PostListView, self).get_context_data(**kwargs)
        context["recommandation_list"] = recommandation_list
        return context


def blogPostLike(request, pk):
    redirect_path = request.POST.get('redirect_path')
    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(redirect_path)

def deletePostView(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    
    return HttpResponseRedirect(reverse('profpage-user'))

def deleteCommentView(request, pk):
    comment = get_object_or_404(PostComment, id=request.POST.get('comment_delete_id'))
    comment.delete()

    return HttpResponseRedirect(reverse('create-comment', args=[str(pk)]))

def followUser(request, pk):
    user_to_follow = get_object_or_404(user_model, id=pk)
    redirect_path = request.POST.get('redirect_path')
    
    # If user already follows, remove follow
    if request.user.followed.filter(id=user_to_follow.id).exists():
        (request.user).followed.remove(user_to_follow)

    else:
        if user_to_follow.is_private:
            # If user to follow is private and there is a request pending remove it
            # because this means that he wants to withdraw it
            if user_to_follow.pending_requests.filter(id=request.user.id).exists():
                user_to_follow.pending_requests.remove(request.user)
            # Else add request
            else:
                user_to_follow.pending_requests.add(request.user)
        # If user i s public follow him
        else:
            (request.user).followed.add(user_to_follow)
        
    return HttpResponseRedirect(redirect_path)

def acceptOrDelteUsersRequest(request, pk):
    user_who_has_requested = get_object_or_404(user_model, id=pk)

    # Get value if user wants to delete or accept request
    accept_or_delete = request.POST.get('accept_or_delete')

    # If logged in user accpets(confirms) remove usre who requested out
    # of pending requests field and add logged in user to requested users
    # followed field(so he follows logged in user)
    if accept_or_delete == "accept":
        request.user.pending_requests.remove(user_who_has_requested)
        user_who_has_requested.followed.add(request.user)
    else:
        request.user.pending_requests.remove(user_who_has_requested)
    
    return HttpResponseRedirect(reverse('activity-page'))

@login_required
def userSavePost(request, pk):
    post = get_object_or_404(Post, id=pk)
    redirect_path = request.POST.get('redirect_path')
    if request.user.saved_posts.filter(id=post.id).exists():
        request.user.saved_posts.remove(post)
    else:
        request.user.saved_posts.add(post)
            
    return HttpResponseRedirect(redirect_path)


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
    
    post_is_saved = True if request.user.saved_posts.filter(id=post_for_comment.id).count() == 1 else False

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
            return HttpResponseRedirect(reverse('create-comment', args=[str(pk)]) )

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
        'post_is_saved': post_is_saved, 
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
    user_for_page = get_object_or_404(user_model, pk=pk)
    logged_in_user_is_following = request.user.followed.filter(id=user_for_page.id).exists()
    context = {
        'user_for_page': user_for_page,
        'user_is_followed': logged_in_user_is_following,
         
    }

    return render(request, 'insta/user_detail.html', context)

class ProfilPageListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "insta/profil_page_by_user.html"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    
    def get_context_data(self, **kwargs):
        
        user_is_marked_list = Post.objects.filter(tagged_people__id=self.request.user.id)
        user_follows_list = self.request.user.followed.all()
        # follows_user_list = self.request.user._set.all()
        

        context = super(ProfilPageListView, self).get_context_data(**kwargs)
        context["user_follows_list"] = user_follows_list
        context["user_is_marked_list"] = user_is_marked_list
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["picture", "caption", "tagged_people"]

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

class SearchResultsView(LoginRequiredMixin, generic.ListView):
    model = user_model
    template_name="insta/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = user_model.objects.filter(username__icontains=query).exclude(username=self.request.user.username)[:50]

        return object_list 

class SearchPageListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "insta/search_page.html"


    def get_queryset(self):
        user_vars = self.request.user.followed.all()
        private_users = user_model.objects.filter(is_private=True)

        return Post.objects.exclude(author=self.request.user).exclude(author__in=user_vars).exclude(author__in=private_users).order_by("-likes")

@login_required
def activityPage(request):
    post_list = request.user.post_set.all()
    followers_list = request.user.followed_field.all()
    # The last user who send a request to logged in user
    # Used to display his pp
    last_user_requested = request.user.pending_requests.last()    
    # If account is private, show pending follow requests for loged in user(if there are some)
    user_number_requests = request.user.pending_requests.all().count()    

    context = {
        'post_list': post_list,
        'followers_list': followers_list,
        'last_user_requested': last_user_requested,
        'user_number_requests': user_number_requests,
        
    }
    return render(request, 'insta/activity_page.html', context)

@login_required
def dontexistPage(request, string):
    context = {
        
    }
    return render(request, 'insta/dont_exist_page.html', context)

