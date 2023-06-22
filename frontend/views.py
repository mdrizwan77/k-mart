from django.shortcuts import render,redirect
from cms.models import Slider
from product.models import ProductCategory, Product, ProductTag
from cms.models import (WebsiteSetting,Slider,Blog,Contact,About)
from django.views import View


def home_page(request):
    """ Home page of k-mart E-com  """
    sliders = Slider.objects.filter(status=True)
    product_categories = ProductCategory.objects.filter(status=True, show_on_homepage=True)
    fashion_products_one = Product.objects.filter(status=True)[0:2]
    fashion_products_two = Product.objects.filter(status=True)[2:4]
    product_tags = ProductTag.objects.filter(status=True)[0:2]
    context = {
        'sliders' : sliders,
        'product_categories' : product_categories,
        'fashion_products_one' : fashion_products_one,
        'fashion_products_two' : fashion_products_two,
        'product_tags' : product_tags
    }
    return render(request, 'home.html', context)

""" Products with category id """
# def product_listing(request, category_id):
#     navigation_categories = ProductCategory.objects.filter(status=True)
#     website_setting = WebsiteSetting.objects.all().last()
#     # products = Product.objects.filter(status=True, product_category=category_id)
#     products = Product.objects.filter(status=True, product_category_id=category_id) # recomended
#     print(products)
#     context = {
#         'navigation_categories' : navigation_categories,
#         'website_setting' : website_setting,
#         'products' : products
#     }
#     return render(request, 'product/product_listing.html', context)

def product_listing(request, product_category_slug=None):
    """ Products with category slug """
    filters = {
        'status':True
    }
    if request.GET.get('search'):
        filters['name__icontains'] = request.GET.get('search')

    if product_category_slug:
        filters['product_category__slug'] = product_category_slug
    products = Product.objects.filter(**filters) # recomended
    context = {
        'products' : products
    }
    return render(request, 'product/product_listing.html', context)


class ProductDetails(View):

    def get(self, request, product_slug):
        try:
            product = Product.objects.get(slug=product_slug)
            similar_products = Product.objects.filter(status=True, product_category=product.product_category).exclude(id=product.id)
            context = {
                'product' : product,
                'similar_products' : similar_products,
            }
            return render(request, 'product/product_details.html', context)
        except Product.DoesNotExist:
            pass

def Contact_page(request):
     """cotact page"""
     if request.method =='POST':
         name=request.POST.get("name")
         mobile=request.POST.get("mobile") 
         email=request.POST.get("email") 
         message=request.POST.get("message")
         information=Contact.objects.create (name=name, email=email ,mobile=mobile, message=message) 
         information.save()
         return redirect("home_page")

     return render(request,'contact/contact.html')         

def about_page(request):
    """about us page """
    abouts =About.objects.filter(status=True)
    context = {
        "abouts":abouts 
    }
    return render(request, "about/about.html", context)

def blog_page(request):
    """ blogs page"""
    blogs = Blog.objects.filter(status=True)
    return render(request, "blog/blog.html", {"blogs": blogs})



