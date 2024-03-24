from django.contrib import admin
from .models import Question, Answer, User, Report

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Report)
