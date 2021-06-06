from django.contrib import admin

# Register your models here.
from .models import *
from ..login_register.models import User
admin.site.register(User)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Cataegory)

