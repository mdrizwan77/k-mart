from product.models import ProductCategory


def navigation_product_categories(request):
    """ For navigation product category dropdown """
    navigation_product_categories = ProductCategory.objects.filter(status=True)
    return { 'navigation_product_categories' : navigation_product_categories }
