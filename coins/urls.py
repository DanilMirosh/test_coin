from django.urls import path

from coins.views import CoinCreateView, CoinsListView, CoinDetailView

urlpatterns = [
    path('coin/', CoinCreateView.as_view()),
    path('all/', CoinsListView.as_view()),
    path('coin/detail/<int:pk>/', CoinDetailView.as_view()),
]
