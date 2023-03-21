from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.
class Course(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  region = models.CharField(max_length=255)
  par = models.IntegerField()
  price = models.IntegerField()
  founded = models.IntegerField()
  website_link = models.CharField(max_length=255)
  profile_picture = models.ImageField(upload_to="uploads/", default="placeholder/placeholder.jpg")
  

  def __str__(self):
    return f"{self.id} {self.name}"

  def get_average(self):
    average_score = Review.objects.filter(course=self).aggregate(Avg('rating'))['rating__avg']

    # MANUAL VERSION BELOW
    # sum_of_reviews = 0
    # for review in reviews:
    #   sum_of_reviews += review.rating
    # average_score = sum_of_reviews / len(reviews)

    if average_score.is_integer():
      return int(average_score)
    else:
      return round(average_score, 1)


  # This ain't working - course rank (get the INDEX of the position in list - should be ok)

  # def get_ranking(self):
  #   courses = Course.objects.all()
  #   list_of_averages = []
  #   for course in courses:
  #     average = course.get_average()
  #     list_of_averages.append(average)
  #   sorted_averages = list_of_averages.sort(reverse=True)
  #   count = 0
  #   for course in sorted_averages:
  #     count += 1
  #     course_rank = count

  #   return course_rank
      
    




class Review(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
  description = models.CharField(max_length=255)

  reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
  
  rating = models.IntegerField()
  date = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.course.name} | {self.reviewer}"




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # related names below should really be something like "user"
    wishlist = models.ManyToManyField(Course, blank=True, null=True, related_name="wishlist")
    played_list = models.ManyToManyField(Course, blank=True, null=True, related_name="played_list")
    friends = models.ManyToManyField(User, blank=True, null=True, related_name="friends")
    
    profile_picture = models.ImageField(upload_to="uploads/", default="placeholder/placeholder.jpg")

    def __str__(self):
      return f"{self.id}: {self.user.username}"
    