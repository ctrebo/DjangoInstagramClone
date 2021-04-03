from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.PostListView.as_view(), name="index"),
    url(r"^(?P<pk>[0-9]+)/create/$", views.postCommentCreate, name="create-comment"),
    url(r"^user/(?P<pk>[0-9]+)$", views.user_detail, name="user-detail"),
    url(r"^profilpage/$", views.ProfilPageListView.as_view(), name="profpage-user"),

]