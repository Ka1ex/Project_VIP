from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.TextField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    