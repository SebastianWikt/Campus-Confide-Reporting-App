# Generated by Django 4.2.10 on 2024-04-26 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_type', models.CharField(choices=[('professors', 'Professors'), ('teaching_assistant', 'Teaching Assistant'), ('homework_assignments', 'Homework Assignments'), ('course_logistics', 'Course Logistics'), ('tests_exams', 'Tests/Exams'), ('others', 'Others')], default='others', max_length=30, verbose_name='Related to')),
                ('title', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(default='', max_length=200)),
                ('file', models.FileField(blank=True, null=True, upload_to='reports/')),
                ('submission_status', models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')], default='New', max_length=30)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='', max_length=200)),
                ('read', models.BooleanField(default=False)),
                ('report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hooknowsapp.report')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdminNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_notes', to='hooknowsapp.report')),
            ],
        ),
    ]
