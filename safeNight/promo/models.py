from datetime import datetime
from django.db import models

# Create your models here.
class Promo(models.Model):
    promo_type = models.TextField(max_length=20)
    promo_date = models.DateTimeField(datetime)
    promo_description = models.CharField(max_length=100)
    