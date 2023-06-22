from django.contrib import admin, messages
from product.models import Product, ProductCategory, ProductTag, ProductVariation, ProductImage


def active_status(modelAdmin, request, queryset):
    """ messages.success -> shows green alert """
    """ messages.error -> shows red alert """
    """ messages.warning -> shows brown alert """
    """ messages.info -> shows green alert """
    try:
        queryset.update(status=True)
        messages.success(request, 'Selected record(s) marked as active')
    except Exception as e:
        messages.error(request, str(e))

def inactive_status(modelAdmin, request, queryset):
    try:
        queryset.update(status=False)
        messages.success(request, 'Selected record(s) marked as active')
    except Exception as e:
        messages.error(request, str(e))

# class ProductImagesInline(admin.TabularInline):
#""" Display Child Form in table format  """
#     model = ProductImage
class ProductImagesInline(admin.StackedInline):
    """ Display child form in row format  """
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}
    list_display = ["name", "product_category", "price", "status"]
    list_filter = ["product_category"]
    search_fields = ["name"]
    inlines = (ProductImagesInline, )
    actions = (active_status, inactive_status)


admin.site.register(Product, ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "status", "show_on_homepage"]
    list_filter = ["name"]
    search_fields = ["name"]


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ["name", "status"]
    list_filter = ["name"]
    search_fields = ["name"]


admin.site.register(ProductVariation, ProductVariationAdmin)


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ["name", "status"]
    list_filter = ["name"]
    search_fields = ["name"]


admin.site.register(ProductTag, ProductTagAdmin)


