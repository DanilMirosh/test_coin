from django.contrib import admin

from coins.models import Coin


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol', 'price', 'market_cap', 'volume_24h', 'percent_change_24h')
    search_fields = ('name', 'symbol')
    list_filter = ('name',)
