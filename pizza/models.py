from django.db import models
from django.contrib.gis.db.models import PointField

class Flavor(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=200,blank=True,null=True)


class PizzaSize(models.Model):
    name = models.CharField(max_length=50,unique=True)
    diameter = models.FloatField()


class Pizza(models.Model):
    pizza_size = models.ForeignKey(PizzaSize,on_delete=models.CASCADE)
    flavor = models.ForeignKey(Flavor,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('pizza_size','flavor')

    def __str__(self):
        return "{} {}".format(self.flavor.name, self.pizza_size.name)


class Customer(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=30,blank=True,null=True)

    class Meta:
        unique_together = ('name', 'phone')

    def __str__(self):
        return "{} ({})".format(self.name, self.id)


class Status(models.Model):
    text = models.CharField(max_length=50,unique=True)
    imutable = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    destination = PointField()
    status = models.ForeignKey(Status,default=1,on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza)




