from django.contrib import admin
from .models import Following, Post, LikedPost, ProfilePic, UserBio, PostComment

admin.site.register(Post)
admin.site.register(Following)
admin.site.register(LikedPost)
admin.site.register(ProfilePic)
admin.site.register(UserBio)
admin.site.register(PostComment)
