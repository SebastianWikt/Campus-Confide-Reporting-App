from django.contrib import admin
from .models import Question, Answer, User, Report, AdminNote, Notification

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Report)
admin.site.register(AdminNote)
admin.site.register(Notification)
