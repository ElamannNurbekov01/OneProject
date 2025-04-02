from django.contrib import admin

from app.models import Category, Car

# Register your models here.
admin.site.register(Category)
admin.site.register(Car)


# shop/admin.py
from django.contrib import admin
from .models import PurchaseRequest

@admin.register(PurchaseRequest)
class PurchaseRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'car__name', 'message')
