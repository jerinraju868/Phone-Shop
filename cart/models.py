from django.db import models
from django.contrib.auth.models import User
from jshop_app.models import Product


class Cartlist(models.Model):
    cart_id = models.CharField(max_length=250, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class Items(models.Model):
    prodt = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cartlist, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.prodt

class Address(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    landmark = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    pincode = models.CharField(max_length=100, unique=True)
    paymentmethod = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.name)