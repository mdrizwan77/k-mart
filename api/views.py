from rest_framework import viewsets, views, response, status
from django.contrib.auth.models import User
from product.models import ProductCategory
from .serializers import (UserSerializer, )
from . import serializers


class UserAuthView():
    pass


class UserView(viewsets.ModelViewSet):
    """ User CRUD Operation """
    serializer_class = serializers.UserSerializer
    queryset = User.objects.filter(is_superuser=False, is_staff=False)



class ProductCategoryView(views.APIView):
    serializer_class = serializers.ProductCategorySerializer

    def get(self, request):
        product_categories = ProductCategory.objects.filter(status=True)
        serializer = self.serializer_class(product_categories, many=True)
        return response.Response(serializer.data)


class ProductCategoryViewSets(viewsets.ModelViewSet):
    """ Product Category API """
    serializer_class = serializers.ProductCategorySerializer
    queryset = ProductCategory.objects.filter(status=True)
    http_method_names = ['get']
