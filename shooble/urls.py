from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('create/', views.create_text_post, name="create"),
    path('search/', views.search_shooble, name="search"),
    path('profile/<str:username>', views.profile_view, name="profile"),
    path('follow/<str:username>', views.follow_user, name="follow"),
    path('unfollow/<str:username>', views.unfollow_user, name="unfollow"),
    path('settings/', views.settings_view, name="settings"),
    path('liked/<str:postID>', views.like_post, name="like_post"),
    path('upload/', views.upload_profile_pic, name="upload_pic"),
    path('delete/<str:postID>', views.delete_post, name="delete_post"),
    path('create-bio/', views.create_bio, name="create_bio"),
    path('is-following/<str:username>', views.is_following, name="is_following"),
    path('is-followed-by/<str:username>', views.is_followed_by, name='is_followed_by'),
    path('make-comment/<str:postID>', views.make_comment, name='make_comment')
]
