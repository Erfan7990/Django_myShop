from django.urls import path
from dashboard.views import *
urlpatterns = [
    path('', DashboardHomeView.as_view(), name='admin_home'),
    path("product-list/", ProductListView.as_view(), name="product_list"),
    path("add-product/", add_products, name="add_product"),
    path("categories-list/", categories, name="categories_list"),
    path("add-category/", add_categories, name="add_categories"),
]
