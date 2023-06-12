from django.db import models


class Coin(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=30, decimal_places=10)
    market_cap = models.DecimalField(max_digits=30, decimal_places=10)
    volume_24h = models.DecimalField(max_digits=30, decimal_places=10)
    percent_change_24h = models.DecimalField(max_digits=30, decimal_places=2)
