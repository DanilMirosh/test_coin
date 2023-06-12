import psycopg2
import requests
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from coins.models import Coin
from coins.permissions import IsOwnerOrReadOnly
from coins.serializers import CoinDetailSerializer, CoinsListSerializer


class CoinCreateView(APIView):
    def get(self, request):
        response = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',
                                headers={'X-CMC_PRO_API_KEY': '3cbe980e-b3f0-4ed6-add3-c43d7062d08b'})
        json_data = response.json()['data']

        coins = []
        for item in json_data:
            coin = Coin()
            coin.name = item['name']
            coin.symbol = item['symbol']
            coin.price = item['quote']['USD']['price']
            coin.market_cap = item['quote']['USD']['market_cap']
            coin.volume_24h = item['quote']['USD']['volume_24h']
            coin.percent_change_24h = item['quote']['USD']['percent_change_24h']
            coins.append(coin)

        # Save coins to Postgres
        conn = psycopg2.connect("dbname=test user=danil ")
        cur = conn.cursor()
        for coin in coins:
            cur.execute(
                "INSERT INTO coins_coin (name, symbol, price, market_cap, volume_24h, percent_change_24h) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (coin.name, coin.symbol, coin.price, coin.market_cap, coin.volume_24h, coin.percent_change_24h))
        conn.commit()
        cur.close()
        conn.close()

        # Return serialized data
        serializer = CoinDetailSerializer(coins, many=True)
        return Response(serializer.data)


class CoinsListView(generics.ListAPIView):
    serializer_class = CoinsListSerializer
    queryset = Coin.objects.all()
    # permission_classes = (IsAuthenticated,)


class CoinDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CoinDetailSerializer
    queryset = Coin.objects.all()
    # permission_classes = (IsOwnerOrReadOnly,)
