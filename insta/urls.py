<<<<<<< HEAD
from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    re_path(r"^$", views.PostListView.as_view(), name="index"),
    re_path(r"^comment/(?P<pk>[0-9]+)/create/$", views.postCommentCreate, name="create-comment"),
    re_path(r"^user/(?P<pk>[0-9]+)$", views.user_detail, name="user-detail"),
    re_path(r"^user/profilpage/$", views.ProfilPageListView.as_view(), name="profpage-user"),
    re_path(r"^post/create/$", views.PostCreateView.as_view(), name="create-post"),
    re_path(r"^post/(?P<pk>[0-9]+)/like/$", views.blogPostLike, name="like-post"),
    re_path(r"^user/(?P<pk>[0-9]+)/follow/$", views.followUser, name="follow-user"),
    re_path(r"^user/(?P<pk>[0-9]+)/follow-profpage/$", views.followUserProfPage, name="follow-user-profpage"),
    re_path(r"^post/(?P<pk>[0-9]+)/like-list-view/$", views.blogPostLikeListView, name="like-post-for-list-view"),
    re_path(r"^user/(?P<pk>[0-9]+)/save/$", views.userSavePost, name="save-post"),
    re_path(r"^user/(?P<pk>[0-9]+)/save-list-view/$", views.userSavePostListView, name="save-post-list-view"),
    re_path(r"^user/(?P<pk>[0-9]+)/update/$", views.updateUser, name="update-user"),
    re_path(r"^search/$", views.SearchResultsView.as_view(), name='search_results'),
    re_path(r"^search-page/$", views.SearchPageListView.as_view(), name='search_page'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r"^user/activity/$", views.activityPage, name='activity-page'),
    re_path(r"^user/(?P<string>[\w\-]+)/$", views.dontexistPage, name='user-dont-exist'),
    re_path(r"^post/(?P<pk>[0-9]+)/delete/$", views.deletePostView, name='delete-post'),
    re_path(r"^comment/(?P<pk>[0-9]+)/comment/$", views.deleteCommentView, name='delete-comment'),
]
=======
from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    re_path(r"^$", views.PostListView.as_view(), name="index"),
    re_path(r"^comment/(?P<pk>[0-9]+)/create/$", views.postCommentCreate, name="create-comment"),
    re_path(r"^user/(?P<pk>[0-9]+)$", views.user_detail, name="user-detail"),
    re_path(r"^user/profilpage/$", views.ProfilPageListView.as_view(), name="profpage-user"),
    re_path(r"^post/create/$", views.PostCreateView.as_view(), name="create-post"),
    re_path(r"^post/(?P<pk>[0-9]+)/like/$", views.blogPostLike, name="like-post"),
    re_path(r"^user/(?P<pk>[0-9]+)/follow/$", views.followUser, name="follow-user"),
    re_path(r"^post/(?P<pk>[0-9]+)/like-list-view/$", views.blogPostLikeListView, name="like-post-for-list-view"),
    re_path(r"^user/(?P<pk>[0-9]+)/save/$", views.userSavePost, name="save-post"),
    re_path(r"^user/(?P<pk>[0-9]+)/update/$", views.updateUser, name="update-user"),
    re_path(r"^search/$", views.SearchResultsView.as_view(), name='search_results'),
    re_path(r"^search-page/$", views.SearchPageListView.as_view(), name='search_page'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r"^user/activity/$", views.activityPage, name='activity-page'),
    re_path(r"^user/(?P<string>[\w\-]+)/$", views.dontexistPage, name='user-dont-exist'),
    re_path(r"^post/(?P<pk>[0-9]+)/delete/$", views.deletePostView, name='delete-post'),
    re_path(r"^comment/(?P<pk>[0-9]+)/delete/$", views.deleteCommentView, name='delete-comment'),
]
>>>>>>> createViewsAndTemplates
