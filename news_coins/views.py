import requests
from django.shortcuts import render


def crypto_news(request):
    url = "https://newsapi.org/v2/everything?q=crypto&sortBy=publishedAt&apiKey=49a969d26da04fb9ad42e70d6a2031a1"
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {'articles': articles}
    return render(request, 'crypto_news.html', context)
