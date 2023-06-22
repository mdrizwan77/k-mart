from django.contrib import admin
from order.models import Order, OrderDetails


class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "mobile", "payment", "status"]
    list_filter = ["status", "payment"]
    search_fields = ["id", "user__first_name"]
    inlines = (OrderDetailsInline, )


admin.site.register(Order, OrderAdmin)
