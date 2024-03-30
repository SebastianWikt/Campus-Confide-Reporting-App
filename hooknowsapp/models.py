from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=200)


class Answer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

class Report(models.Model):
    submission_types = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='', max_length=200)
    file = models.FileField(upload_to='reports/')
    submission_status = models.CharField(max_length=30, choices=submission_types, default='New')

class AdminNote(models.Model):
    report = models.ForeignKey(Report, related_name='admin_notes', on_delete=models.CASCADE)
    note = models.TextField()