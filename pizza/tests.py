from django.test import TestCase
from pizza.models import Order, Customer, Pizza, Status
from django.urls import reverse

class TestOrderViewSet(TestCase):

    fixtures = ['pizza']

    def test_get(self):
        url = reverse('orders-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data)

    def test_delete(self):
        print(Order.objects.all().first().id)
        url = reverse('orders-detail',args=[Order.objects.all().first().id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_post(self):
        url = reverse('orders-list')

        data = {
            'customer': Customer.objects.all().first().id,
            'destination': 'POINT(-47.92972 15.77972 )',
            'pizzas': Pizza.objects.all().values_list('id',flat=True)
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data)

    def test_patch(self):
        url = reverse('orders-detail', args=[Order.objects.all().first().id])

        response = self.client.patch(url)
        self.assertEqual(response.status_code, 200)