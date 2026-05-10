from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import ShortText


class RandomTextAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('random_text')

    def test_random_text_returns_text_when_available(self):
        ShortText.objects.create(text='Try something new')
        ShortText.objects.create(text='Take a short walk')

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('text', response.data)
        self.assertIn(response.data['text'], ['Try something new', 'Take a short walk'])

    def test_random_text_returns_404_when_no_texts(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'No short texts available.')
