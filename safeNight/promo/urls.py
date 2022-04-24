from rest_framework import routers
from .api import PromoViewSets

router = routers.DefaultRouter()
router.register('api/promo', PromoViewSets, 'promo')

urlpatterns = router.urls