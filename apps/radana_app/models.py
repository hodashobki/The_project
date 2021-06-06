from django.db import DefaultConnectionProxy, models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from ..login_register.models import User
from decimal import Decimal
# Create your models here.

class Cataegory(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Item(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    available_quantity=models.IntegerField()
    image=models.CharField(max_length=255)
    categories=models.ForeignKey(Cataegory,related_name='items',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class Order(models.Model):
    # quantity=models.IntegerField(default=0)
    user=models.ForeignKey(User, related_name="orders",on_delete=models.CASCADE)
    total_price=models.FloatField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.total_price
class Cart(models.Model):
    user=models.ForeignKey(User,related_name='user_cart',on_delete=CASCADE)
    item=models.ForeignKey(Item,related_name='cart_item',default=1,on_delete=CASCADE)
    quantity=models.IntegerField(default=1)
    deleted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
# def fliter_items(current_user):
#     cart=Cart.objects.get(user=current_user)
#     items=cart.items.all()
#     m=[]
#     for item in items:
#         s=len(cart.items.filter(item))
#         m.append(s)
#     return m
# def addToCart(user_id,ItemToAdd):
#     cart=Cart.objects.create(user=user_id)
#     cart.items.add(ItemToAdd)
# def available_quantity(cart):
#     items=cart.items.all()
#     x=[]
#     for item in items:
#         x.append(item.available_quantity)
#     return



# quan = "itemid#quantity" ,  "2#4" , "3#6" 