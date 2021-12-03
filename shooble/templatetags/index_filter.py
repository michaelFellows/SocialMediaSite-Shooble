from django import template

register = template.Library()


@register.filter()
def index(list1, i):
    return list1[int(i)]


@register.filter()
def get_liked(list1):
    return list1.is_liked_by_user
