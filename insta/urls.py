from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    re_path(r"^$", views.PostListView.as_view(), name="index"),
    re_path(r"^(?P<pk>[0-9]+)/create/$", views.postCommentCreate, name="create-comment"),
    re_path(r"^user/(?P<pk>[0-9]+)$", views.user_detail, name="user-detail"),
    re_path(r"^profilpage/$", views.ProfilPageListView.as_view(), name="profpage-user"),
    re_path(r"^post/create/$", views.PostCreateView.as_view(), name="create-post"),
    re_path(r"^post/(?P<pk>[0-9]+)/like/$", views.blogPostLike, name="like-post"),
    re_path(r"^post/(?P<pk>[0-9]+)/follow/$", views.followUser, name="follow-user"),
    re_path(r"^post/(?P<pk>[0-9]+)/like-list-view/$", views.blogPostLikeListView, name="like-post-for-list-view"),
    re_path(r"^user/(?P<pk>[0-9]+)/update/$", views.updateUser, name="update-user"),
    re_path(r"^search/$", views.SearchResultsView.as_view(), name='search_results'),
    re_path(r"^search-page/$", views.SearchPageListView.as_view(), name='search_page'),


]