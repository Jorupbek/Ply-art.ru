from django.urls import path
from shop.views import ProductDetail, CategoryListView, tagged

urlpatterns = [
    path('collection/', CategoryListView.as_view(), name='product_list'),
    path('collection/<slug:category_slug>/', CategoryListView.as_view(), name='product_by_category'),
    path('collection/tags/<slug:slug>/', tagged, name="tagged"),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
]
