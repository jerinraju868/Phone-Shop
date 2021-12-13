from django.contrib import admin

# Register your models here.
from cart.models import Cartlist, Items

admin.site.register(Cartlist)
admin.site.register(Items)