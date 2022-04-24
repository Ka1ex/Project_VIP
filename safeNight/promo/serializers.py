from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from promo.models import Promo

#Promo Serializer
class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'