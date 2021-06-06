from decimal import Context
from django.db.models.fields import NullBooleanField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import *
from .import models
from ..login_register.models import User

# Create your views here.
def index(request):
    if 'cart' in request.session:
        request.session['cart_item_count'] = sum(request.session['cart'].values())
    else:
        request.session['cart_item_count'] = 0       
        context={
            "item1":Item.objects.get(id=1),
            "item2":Item.objects.get(id=2),
            "item3":Item.objects.get(id=3),
        }
        return render(request,'store.html',context)
def item_detailes(request,item_id):
    context={
        "item":Item.objects.get(id=item_id)
    }
    return render(request,'item.html',context)
def items(request):
    context={
        'categories':Cataegory.objects.all(),
        'items':Item.objects.all()
    }
    return render (request,'shop.html',context)
def category(request,cat_id):
    category=Cataegory.objects.get(id=cat_id)
    context={
        'name':category,
        'category':category.items.all()
    }
    return render (request,'category.html',context)
def add_to_cart(request,item_id):
    item=Item.objects.get(id=item_id)
    current_user=User.objects.get(id=request.session['user_id'])
    item=Item.objects.get(id=item_id)
    if item.available_quantity-1 >0:
        Cart.objects.create(user=current_user,item=item,quantity=1,deleted=False)
        item.available_quantity-=1
    else:
        return HttpResponse('The quantity you want is bigger than the availabe quantity')
    return redirect('/items')
def add_quantity(request,item_id):
    quantity=int(request.POST['quantity'])
    current_user=User.objects.get(id=request.session['user_id'])
    item=Item.objects.get(id=item_id)
    if item.available_quantity-quantity >0:
        Cart.objects.create(user=current_user,item=item,quantity=quantity,deleted=False)
        item.available_quantity-=quantity
    else:
        return HttpResponse('The quantity you want is bigger than the availabe quantity')
    return redirect('/items')

def autocomplete(request):
    if 'term' in request.GET:
        sr= Item.objects.filter(name__istartswith=request.GET['term'])
        names=list()
        for i in sr:
            names.append(i.name)
            # return render (request,"search.html",{'sr':sr})
        return  JsonResponse(names , safe=False)

    return render (request,"search.html")


def searchhhhh(request):
    id=Item.objects.filter(name=request.POST['search']).first().id
    return redirect(f"/items/{id}")


def remove_item(request,item_id,item_quantity,item_idd):
    item_delete=Item.objects.get(id=item_idd)
    cart=Cart.objects.get(id=item_id)
    cart.delete()
    item_delete.available_quantity+=item_quantity
    return redirect('/checkout')
def checkout(request):
    current_user=User.objects.get(id=request.session['user_id'])
    cart=current_user.user_cart.filter(deleted=False)
    total_price=0
    total_items=0
    for item in cart:
        total_price+=item.item.price*item.quantity
    for item in cart:
        total_items+=item.quantity
    request.session['total_cost']=total_price
    request.session['total_items']=total_items
    context={
        'CartItems':cart,
        'total_cost':total_price,
    
    }
    return render(request,'checkout.html',context)
def purchase(request):
    total_cost=request.session['total_cost']
    total_sum=request.session['total_items']
    current_user=User.objects.get(id=request.session['user_id'])
    cart=current_user.user_cart.filter(deleted=False)
    Order.objects.create(user=current_user,total_price=total_cost)
    cart.delete()
    context={
        'cost':total_cost,
        'sum':total_sum
    }
    return render (request,'thank.html',context)
def about(request):
    return render(request,'about_us.html')
def logout(request):
    request.session.clear()
    return redirect ('/')

