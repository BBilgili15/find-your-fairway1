from django import template

register = template.Library()

# Checking if course on lists
@register.filter
def on_wishlist(user, course):
    return user.profile.wishlist.filter(id=course.id).exists()

@register.filter
def on_playedlist(user, course):
    return user.profile.played_list.filter(id=course.id).exists()
