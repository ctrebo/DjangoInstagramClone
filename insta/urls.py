from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    re_path(r"^$", views.PostListView.as_view(), name="index"),
    re_path(r"^comment/(?P<pk>[0-9]+)/create/$", views.postCommentCreate, name="create-comment"),
    re_path(r"^comment/(?P<pk>[0-9]+)/create/mobile/$", views.postCommentCreateMobile, name="create-comment-mobile"),
    re_path(r"^user/(?P<pk>[0-9]+)$", views.user_detail, name="user-detail"),
    re_path(r"^user/profilpage/$", views.ProfilPageListView.as_view(), name="profpage-user"),
    re_path(r"^post/create/$", views.PostCreateView.as_view(), name="create-post"),
    re_path(r"^post/(?P<pk>[0-9]+)/like/$", views.postLike, name="like-post"),
    re_path(r"^comment/(?P<pk>[0-9]+)/like/$", views.postCommentLike, name="like-postcomment"),
    re_path(r"^user/(?P<pk>[0-9]+)/follow/$", views.followUser, name="follow-user"),
    re_path(r"^user/(?P<pk>[0-9]+)/followhashtag/$", views.followHashtag, name="follow-hashtag"),
    re_path(r"^user/(?P<pk>[0-9]+)/accpet-or-delete/$", views.acceptOrDeleteUsersRequest, name="accpet-or-delete-request"),
    re_path(r"^user/(?P<pk>[0-9]+)/remove-tag/$", views.removeTag, name="remove-tag"),
    re_path(r"^user/(?P<pk>[0-9]+)/save/$", views.userSavePost, name="save-post"),
    re_path(r"^user/(?P<pk>[0-9]+)/update/$", views.updateUser, name="update-user"),
    re_path(r"^search/$", views.SearchResultsView.as_view(), name='search_results'),
    re_path(r"^search-page/$", views.SearchPageListView.as_view(), name='search_page'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r"^user/activity/$", views.activityPage, name='activity-page'),
    re_path(r"^object/(?P<string>[\w\-]+)/$", views.dontexistPage, name='object-dont-exist'),
    re_path(r"^post/(?P<pk>[0-9]+)/delete/$", views.deletePostView, name='delete-post'),
    re_path(r"^comment/(?P<pk>[0-9]+)/delete/$", views.deleteCommentView, name='delete-comment'),
    re_path(r"^stories/(?P<pk>[0-9]+)/view/$", views.story_of_user, name='stories-user'),
    re_path(r"^stories/create/$", views.StoryCreateView.as_view(), name='create-stories'),
    re_path(r"^hashtag/(?P<pk>[0-9]+)/view/$", views.HashtagDetailView.as_view(), name='hashtag-detail'),
]
