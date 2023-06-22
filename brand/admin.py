from django.contrib import admin
from . models import Brand



class BrandAdmin(admin.ModelAdmin):
   list_display = ['name', 'status']
   list_filter = ['status']
   search_fields = ['name']




