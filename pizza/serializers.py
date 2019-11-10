from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ValidationError
from pizza.models import Order, Status

class OrderSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Order
        geo_field = 'destination'
        fields = ('id','customer','destination','pizzas','status')

    def validate_status(self, value):
        if self.instance and value in Status.objects.filter(imutable=True) :
            raise ValidationError("The actual delivery status is not mutable.")
        return value