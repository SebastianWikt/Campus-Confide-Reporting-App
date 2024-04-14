from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Report, Notification
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hooknows.settings')
django.setup()


# Create your tests here.

class LogInTests(TestCase):
    def test_login(self):
        self.user = User.objects.create_user(username='user', password="pass")
        login_successful = self.client.login(username='user', password='pass')
        self.assertTrue(login_successful)

        response = self.client.get(reverse('login'), follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, reverse('home'))


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
        self.assertEqual(response.status_code, 200)

class TestHomeViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home') 
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
    def test_anonymous(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hooknowsapp/homepage.html')
        self.assertIsNone(response.context['notifications'])  

    def test_staff(self):
        self.user.is_staff = True
        self.user.save()
        self.client.login(username='testuser', password='testpassword')
        
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hooknowsapp/homepage.html')
        self.assertIsNone(response.context['notifications']) 

    def test_user_wo_notifications(self):
        self.client.login(username='testuser', password='testpassword')
        
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hooknowsapp/homepage.html')
        self.assertEqual(list(response.context['notifications']), [])  # Ensure that 'notifications' is an empty list.

    def test_user_notifications(self):
        self.client.login(username='testuser', password='testpassword')
        notification = Notification.objects.create(user=self.user, read=False, message='Test Notification')
        
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hooknowsapp/homepage.html')
        self.assertIn(notification, response.context['notifications']) 
    
class TestLogoutView(TestCase):
    
    def test_logout(self):
        self.client = Client()
        self.logout_url = reverse('logout')  # Replace 'logout' with the actual name of the logout URL pattern.
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.assertIn('_auth_user_id', self.client.session)
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, '/', status_code=302)
        self.assertNotIn('_auth_user_id', self.client.session)