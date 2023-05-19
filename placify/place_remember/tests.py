from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth
from .models import Memory
from .forms import MemoryForm
from .views import get_vk_profile


class MemoryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.client.login(username='testuser',
                          password='testpassword')
        self.memory = Memory.objects.create(user=self.user,
                                            title='Test Memory',
                                            comment='Test Comment',
                                            latitude='12.345',
                                            longitude='67.890')
        self.form_data = {'title': 'New Memory',
                          'comment': 'New Comment',
                          'latitude': '12.345',
                          'longitude': '67.890'}
        access_token = ("vk1.a.xz5Xtf-e6rt0PUGoPAHnnKrAF"
                        "S6bZrpXTAM6Ivv5qWNYpLHR5JlA9RzKQ"
                        "OttzIJyvg3gs5kANfbX1UZyXQaaByZTA"
                        "qYwBExPofYxnjVzF__qw5UJdO9a6OU35"
                        "LTJAqtugtRexE0pczOxWBfUP8izmilCR"
                        "C1XOPO-NnRZq39PQQNFm1VfPpvgDZlEQ"
                        "cKL_FHuwEpFdXzclfbJzTTgHwJguw"
                        )
        UserSocialAuth.objects.create(user=self.user,
                                      provider='vk-oauth2', uid='271682919',
                                      extra_data={
                                          'access_token': access_token
                                          })
        request_factory = RequestFactory()
        request = request_factory.get('/')
        request.user = self.user
        self.vk_user = get_vk_profile(request)

    def test_get_vk_profile_authenticated(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['data'])

    def test_get_vk_profile_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context['data'])

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'place_remember/index.html')

    def test_profile(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'place_remember/profile.html')
        self.assertEqual(response.context['data'], self.vk_user)
        self.assertIn(self.memory, response.context['memories'])

    def test_add_memory_get(self):
        response = self.client.get(reverse('add_memory'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'place_remember/add_memory.html')
        self.assertIsInstance(response.context['form'], MemoryForm)
        self.assertEqual(response.context['data'], self.vk_user)

    def test_add_memory_post(self):
        response = self.client.post(reverse('add_memory'), data=self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/profile')
        self.assertTrue(Memory.objects.filter(title='New Memory').exists())
