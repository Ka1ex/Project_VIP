from django.db import models

# Create your models here.
class Business(models.Model):
    business_name = models.TextField(max_length=30)
    business_address = models.TextField(max_length=100)
    business_website = models.SlugField(max_length=100)
    venue_type = models.TextField(max_length=8)