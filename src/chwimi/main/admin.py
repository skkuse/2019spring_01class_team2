from django.contrib import admin
# Register your models here.
from .models import Product, ListProduct

admin.site.register(Product)
admin.site.register(ListProduct)