from django.db import models

# Create your models here.
COIN_TYPES = (('Bitcoin', 'Bitcoin'), ('Litecoin', 'Litecoin'), ('Ripple', 'Ripple'), ('Ethereum', 'Ethereum'), ('Dogecoin', 'Dogecoin'))


class Info(models.Model):
    name = models.CharField(max_length=30)
    website = models.CharField(max_length=100)
    coins = models.CharField(max_length=30, choices=COIN_TYPES)
# coins2 = models.Select(choices = COIN_TYPES)
    info = models.Manager()

    def __str__(self):
        return self.name