from . import views
from django.urls import path

urlpatterns = [
    path("details/<int:id>", views.course, name="course_details"),

    # below is url to add review
    path("<int:id>/add_review", views.add_review, name="add_review"),
    # below is url to take you to review page
    path("details/<int:id>/review", views.leave_review, name="leave_review")
]
