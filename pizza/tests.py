from django.test import TestCase
from pizza.models import Order, Customer, Pizza, Status, PizzaSize, Flavor
from pizza.serializers import OrderSerializer
# from django.contrib.gis.geos import GEOSGeometry
from django.urls import reverse

class TestOrderViewSet(TestCase):

    fixtures = ['pizza']

    def test_get(self):
        url = reverse('orders-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data)

    def test_delete(self):
        url = reverse('orders-detail',args=[Order.objects.first().id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_post(self):
        url = reverse('orders-list')

        data = {
            'customer': Customer.objects.first().id,
            'destination': 'POINT(-47.92972 15.77972 )',
            'pizzas': Pizza.objects.all().values_list('id',flat=True)
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_patch(self):
        url = reverse('orders-detail', args=[Order.objects.first().id])
        pizzas = list(Pizza.objects.filter(flavor__name='pepperoni').values_list('id', flat=True))
        data = {
            'customer': Customer.objects.all().first().id,
            # Uses list cast because PATCH needs content_type='application/json' and Simplejson does not serializes ValuesListQuerySet
            # as described in https://code.djangoproject.com/ticket/8090
            'pizzas': pizzas
        }
        response = self.client.patch(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(Order.objects.first().pizzas.all().values_list('id', flat=True)), pizzas)


class TestOrderSerializer(TestCase):
    fixtures = ['pizza']

    def test_validate_status(self):
        imutable = Status.objects.create(**{'text': 'ImmutableStatus', 'imutable': True})
        mutable = Status.objects.create(**{'text': 'MutableStatus', 'imutable': False})
        order = Order.objects.first()
        order.status = imutable
        order.save()
        self.assertFalse(
            OrderSerializer(
                order,
                data={'status': mutable.id}
            ).is_valid()
        )
        order.status = mutable
        order.save()
        self.assertTrue(
            OrderSerializer(
                order,
                data={
                    'customer': Customer.objects.all().first().id,
                    'destination': 'POINT(-47.92972 15.77972 )',
                    'pizzas': Pizza.objects.all().values_list('id', flat=True),
                    'status': mutable.id
                }
            ).is_valid()
        )


class TestPizzaViewSet(TestCase):
    #Only get and head are allowed
    fixtures = ['pizza']

    def test_get(self):
        url = reverse('pizzas-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data)


class TestStatusViewSet(TestCase):
    #Only get and head are allowed
    fixtures = ['pizza']

    def test_get(self):
        url = reverse('statuses-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data)


class TestCustomerViewSet(TestCase):

    fixtures = ['pizza']
    #delete is not allowed
    def test_get(self):
        url = reverse('customers-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data)

    def test_post(self):
        url = reverse('customers-list')

        data = {
            'name': 'Vitor Silva',
            'phone': '999999999'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_patch(self):
        url = reverse('customers-detail', args=[Customer.objects.first().id])
        data = {
            'phone': '66666666'
        }
        response = self.client.patch(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Customer.objects.first().phone, data['phone'])