from django.contrib import admin
from .models import Stock
# Register your models here.

@admin.register(Stock) # указывает для какого класса наша админка
class StockAdmin(admin.ModelAdmin): # обязательно наследуемся от admin.ModelAdmin
    pass
