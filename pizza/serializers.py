from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer, ValidationError
from pizza.models import Order, Status, Pizza, Customer

class OrderSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Order
        geo_field = 'destination'
        fields = ('id','customer','destination','pizzas','status')

    def validate_status(self, value):
        if self.instance and self.instance.status.imutable == True:
            raise ValidationError("The actual delivery status is not mutable.")
        return value


class PizzaSerializer(ModelSerializer):

    class Meta:
        model = Pizza
        fields = ('id','flavor','pizza_size')


class StatusSerializer(ModelSerializer):

    class Meta:
        model = Status
        fields = ('id','text','imutable')


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id','name','phone')