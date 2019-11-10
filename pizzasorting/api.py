from rest_framework import routers
from pizza.views import OrderViewset

router = routers.DefaultRouter()
router.register(r'orders', OrderViewset)