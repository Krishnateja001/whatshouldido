from django.urls import path

from .views import random_text, random_text_page

urlpatterns = [
    path('', random_text_page, name='random_text_page'),
    path('api/random-text/', random_text, name='random_text'),
]
