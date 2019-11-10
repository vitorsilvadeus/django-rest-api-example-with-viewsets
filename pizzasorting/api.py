from rest_framework import routers
from pizza.views import OrderViewset

router = routers.DefaultRouter()
router.register(r'orders', OrderViewset,basename='orders')
router.register(r'pizzas', OrderViewset,basename='pizzas')
router.register(r'statuses', OrderViewset,basename='statuses')
router.register(r'customers', OrderViewset,basename='customers')