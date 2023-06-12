from rest_framework import serializers

from coins.models import Coin


class CoinsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('name', 'symbol', 'price')


class CoinDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Coin
        fields = ('id', 'name', 'symbol', 'price', 'market_cap', 'volume_24h', 'percent_change_24h', 'user')
