from django.test import TestCase, Client
from django.urls import reverse
from wmgsis.models import Graduate
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.health_url = reverse('health')
        self.demographic_url = reverse('demographic')
        self.success_url = reverse('success')
        self.satisfaction_url = reverse('satisfaction')
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        
        Graduate.objects.create(
            graduate_name = 'name',
            cohort = '2023',
            salary = '30000',
            city = 'city',
            activity = 'activity',
            degree_classifcation = 'grade'
        )



    #def test_manage_POST_adds_graduate(self):


    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_delete_GET(self):
        client = Client()
        response = client.get(reverse('delete_graduate', args=[1]))
        self.assertEquals(response.status_code, 302)
       

    def test_health_GET(self):
        response = self.client.get(self.health_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'health.html')


    def test_demographic_GET(self):
        response = self.client.get(self.demographic_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'demographic.html')

    def test_success_GET(self):
        response = self.client.get(self.success_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'success.html')

    def test_satisfaction_GET(self):
        response = self.client.get(self.satisfaction_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'satisfaction.html')

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html/')

    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')






