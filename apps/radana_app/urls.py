from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('items',views.items),
    path('items/<int:item_id>',views.item_detailes),
    path('items/<int:item_id>/quantity',views.add_quantity),
    path('remove/<int:item_id>/<int:item_quantity>/<int:item_idd>',views.remove_item),
    path('items/category/<int:cat_id>',views.category),
    path('checkout',views.checkout),
    path('items/<int:item_id>/add',views.add_to_cart),
    path('checkout/purchase',views.purchase),
    path('About_us',views.about),
    path('logout',views.logout),
    path('searchhhhh',views.searchhhhh),
    path('autocomplete',views.autocomplete , name='autocomplete'),
]