from django.contrib import admin

# Register your models here.
from .models import ShippingAddress,Order,OrderItem
from django.contrib.auth.models import User
#register
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
class OrderItemInline(admin.StackedInline):
    model=OrderItem
    extra=0

class OrderAdmin(admin.ModelAdmin):
    model=Order
    readonly_fields=["date_ordered"]
    fields=["user","full_name","email","shipping_address","amount_paid","date_ordered","shipped","date_shipped"]
    inlines=[OrderItemInline]

admin.site.unregister(Order)

admin.site.register(Order,OrderAdmin)