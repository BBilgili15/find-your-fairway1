from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  region = models.CharField(max_length=255)
  par = models.IntegerField()
  price = models.IntegerField()
  average_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  # Why do the above validators do nothing? I can still do a review of 6.
  founded = models.IntegerField()
  website_link = models.CharField(max_length=255)
  # Reviews

  def __str__(self):
    return f"{self.id} {self.name}"
  

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

    wishlist = models.ManyToManyField(Course, blank=True, null=True, related_name="wishlist")
    played_list = models.ManyToManyField(Course, blank=True, null=True, related_name="played_list")

    def __str__(self):
      return f"{self.id}"
    