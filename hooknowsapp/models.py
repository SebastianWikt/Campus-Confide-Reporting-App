from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=200)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)


class User(models.Model):
    is_staff = models.BooleanField(default=False)

class Report(models.Model):
    title = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=200)
    file = models.FileField(upload_to='reports/')