from django.urls import path

from news_coins.views import crypto_news

urlpatterns = [
    path('news/', crypto_news),
]
