from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="information_home"),
    path('my-courses/<int:id>', views.my_courses, name="information_my_courses"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.register, name="register"),

    # Making add to wishlist/played list

    # ADDED/REMOVED THE / AT THE END OF THE URL

    path('<int:id>/add_wishlist', views.add_wishlist, name="course_add_wishlist"),
    path('<int:id>/remove_wishlist', views.remove_wishlist, name="course_remove_wishlist"),
    path('<int:id>/add_playedlist', views.add_playedlist, name="course_add_playedlist"),
    path('<int:id>/remove_playedlist', views.remove_playedlist, name="course_remove_playedlist")
]
