from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    textBody = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    numberOfLikes = models.IntegerField(default=0)

    def __str__(self):
        return self.textBody


class ProfilePic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to='images', default=None)

    def __str__(self):
        if self.user:
            return self.user.username + "'s profile picture"
        else:
            return str(self.id)


class Following(models.Model):
    userFollower = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # the user that is a follower
    userID_following = models.IntegerField()

    def __str__(self):
        return str(self.userFollower.username) + " is following " + str(self.userID_following)


class LikedPost(models.Model):
    user_liking = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_liked_by_user = models.BooleanField(default=False)

    def __str__(self):
        if self.is_liked_by_user:
            liked = " liked "
        else:
            liked = " has not liked "
        return str(self.user_liking) + liked + str(self.post) + " by " + str(self.post.author.username)


class UserBio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    bio = models.TextField(max_length=256, default=None)

    def __str__(self):
        return self.user.username + " bio"

