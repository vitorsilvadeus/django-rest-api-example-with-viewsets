from rest_framework import viewsets
from rest_framework.response import Response
from pizza.models import Order
from pizza.serializers import OrderSerializer

class OrderViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'patch']
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = ('id','status','customer')

