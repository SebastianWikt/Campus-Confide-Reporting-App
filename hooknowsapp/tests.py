from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Report
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hooknows.settings')
django.setup()


# Create your tests here.
"""
class LogInTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password="pass")
    def test_login(self):
        self.client.login_view(username='user', password='pass')
        response = self.client.get(reverse('login'), follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, reverse('home'))
"""
class ReportTestCases(TestCase):
    def test_view_report_submitted(self):
        response = self.client.get(reverse('create_report'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hooknowsapp/create_report.html')

    def test_view_reports(self):
        response = self.client.get(reverse('view_reports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hooknowsapp/view_reports.html')

    def test_create_report(self):
        report_data = {
            'title': 'report',
            'slug': 'rep'
        }
        response = self.client.post(reverse('create_report'), report_data, follow=True)
        #self.assertRedirects(response, reverse('report_submitted'))
        self.assertEqual(response.status_code, 200)

# class TestViews(TestCase):
    