from django import template

register = template.Library()


@register.filter()
def index(list1, i):
    return list1[int(i)]


@register.filter()
def get_liked(list1):
    return list1.is_liked_by_user


@register.filter()
def get_profile_pic(text_post):
    return text_post.author.profilepic_set.get().profile_pic.url


@register.filter()
def user_has_liked(index_of_text_posts, user):
    return index_of_text_posts.likedpost_set.filter(user_liking=user, post=index_of_text_posts)
