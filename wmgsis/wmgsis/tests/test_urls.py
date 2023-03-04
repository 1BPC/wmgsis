from django.test import SimpleTestCase
from django.urls import reverse, resolve
from wmgsis.views import index, health, demographic, manage, register, satisfaction, success, settings, delete_graduate


class TestUrls(SimpleTestCase):

    def test_delete_url_resolves(self):
        url = reverse('delete_graduate', args=[int])
        self.assertEquals(resolve(url).func, delete_graduate)

    def test_index_url_resolves(self):
       url = reverse('index')
       self.assertEquals(resolve(url).func, index)

    def test_health_url_resolves(self):
        url = reverse('health')
        self.assertEquals(resolve(url).func, health)
   
    def test_register_url_resolves(self):
       url = reverse('register')
       self.assertEquals(resolve(url).func, register)

    def test_manage_url_resolves(self):
        url = reverse('manage')
        self.assertEquals(resolve(url).func, manage)

    def test_demographic_url_resolves(self):
        url = reverse('demographic')
        self.assertEquals(resolve(url).func, demographic)

    def test_satisfaction_url_resolves(self):
        url = reverse('satisfaction')
        self.assertEquals(resolve(url).func, satisfaction)

    def test_success_url_resolves(self):
        url = reverse('success')
        self.assertEquals(resolve(url).func, success)

    def test_settings_url_resolves(self):
        url = reverse('settings')
        self.assertEquals(resolve(url).func, settings)
    

