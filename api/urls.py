from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('product_categories', views.ProductCategoryViewSets)


urlpatterns = [
    path('', include(router.urls)),
    path('product_categories_apiview', views.ProductCategoryView.as_view()),
]
