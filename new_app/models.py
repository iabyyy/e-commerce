from datetime import datetime
from tkinter.constants import CASCADE

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.
class Login(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Customer(models.Model):
    User = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='customer')
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()


    def __str__(self):
        return self.name


class Seller(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='seller')
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    seller_id = models.CharField(max_length=6)
    photo = models.FileField(upload_to='document/')

    def __str__(self):
        return self.name


class Products(models.Model):
    photo = models.FileField(upload_to='document/')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)
    date = models.DateField(default=datetime.now,blank=False)
    seller = models.ForeignKey(Seller,on_delete=models.DO_NOTHING,null=True)


    def __str__(self):
        return self.name


class CartItem(models.Model):
    User = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    pay = models.IntegerField(default=0)


class Details(models.Model):
    cart = models.ForeignKey(CartItem, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    address = models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    status = models.IntegerField(default=0)



class Payment(models.Model):
    details = models.ForeignKey(Details,on_delete=models.DO_NOTHING)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiry_date = models.CharField(max_length=5)




