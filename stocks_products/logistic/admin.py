from django.contrib import admin
from .models import StockProduct, Stock, Product
# Register your models here.
admin.site.register(Stock)
admin.site.register(StockProduct)
admin.site.register(Product)