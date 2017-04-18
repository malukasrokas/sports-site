from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_in_detail, name="post_in_detail"),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^forum/$', views.forum_list, name='forum_list'),
    url(r'^forumpost/(?P<pk>\d+)/$', views.forumpost_detail, name='forumpost_detail'),
    url(r'^forumpost/new/$', views.new_forumpost, name='new_forumpost'),
    url(r'^forumpost/edit/(?P<pk>\d+)/$', views.edit_forumpost, name='edit_forumpost'),
    url(r'^forumpost/(?P<pk>\d+)/remove/$', views.remove_forumpost, name='remove_forumpost'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.remove_news_comment, name='remove_news_comment'),
    url(r'^forumpost/(?P<pk>\d+)/comment/$', views.add_comment_to_forumpost, name='add_comment_to_forumpost'),
    url(r'^forumpost/(?P<pk>\d+)/comment/remove/$', views.remove_forum_comment, name='remove_forum_comment'),
    url(r'^teams/$', views.teams, name='teams'),
    url(r'^teams/new/$', views.add_team, name='add_team'),
    url(r'^teams/summary/(?P<pk>\d+)/$', views.team_summary, name="team_summary"),
    url(r'^teams/players/$', views.add_player, name='add_player'),
]
