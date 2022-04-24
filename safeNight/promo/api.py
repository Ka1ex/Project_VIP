from promo.models import Promo
from rest_framework import viewsets, permissions
from .serializers import PromoSerializer

#Promo Viewset
class PromoViewSets(viewsets.ModelViewSet):
    queryset = Promo.objects.all()
    permissions_classses = [
        permissions.AllowAny
    ]
    serializer_class = PromoSerializer