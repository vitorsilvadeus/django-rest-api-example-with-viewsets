from rest_framework import viewsets
from pizza.models import Order, Pizza, Customer, Status
from pizza.serializers import OrderSerializer, PizzaSerializer, CustomerSerializer, StatusSerializer

class OrderViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = ('status','customer')


class PizzaViewset(viewsets.ModelViewSet):
    http_method_names = ['get','head']
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filterset_fields = ('flavor','pizza_size')


class CustomerViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'patch']
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_fields = ('name','phone')


class StatusViewset(viewsets.ModelViewSet):
    http_method_names = ['get','head']
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filterset_fields = ('text')

