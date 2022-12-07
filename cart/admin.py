from django.contrib import admin

# Register your models here.
from cart.models import Cartlist, Items, Address

admin.site.register(Cartlist)
admin.site.register(Items)
admin.site.register(Address)