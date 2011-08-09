from django.contrib import admin
from models import *

class ItemOrderInline(admin.TabularInline):
   model = ItemOrder

class ItemAdmin(admin.ModelAdmin):
   model = Item
   search_fields = ['name']
   inlines = [ItemOrderInline]

class OrderAdmin(admin.ModelAdmin):
   model = Order
   search_fields = ['id']
   inlines = [ItemOrderInline]

admin.site.register(Item,ItemAdmin)
admin.site.register(Customer)
admin.site.register(Order,OrderAdmin)
admin.site.register(Payment)
admin.site.register(ItemOrder)
admin.site.register(GoldSmith)
admin.site.register(GoldSmithItemOrder)
