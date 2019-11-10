from rest_framework import routers
from pizza.views import OrderViewset, PizzaViewset, StatusViewset, CustomerViewset

router = routers.DefaultRouter()
router.register(r'orders', OrderViewset,basename='orders')
router.register(r'pizzas', PizzaViewset,basename='pizzas')
router.register(r'statuses', StatusViewset,basename='statuses')
router.register(r'customers', OrderViewset,basename='customers')