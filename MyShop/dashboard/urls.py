from django.urls import path
from dashboard.views import *
urlpatterns = [
    path('', DashboardHomeView.as_view(), name='admin_home'),
    path("product-list/", ProductListView.as_view(), name="product_list"),
    path("add-product/", add_products.as_view(), name="add_product"),
    path("edit-product/<slug>", EditProduct.as_view(), name="edit_product"),
    path("delete-product/<slug>", DeleteProduct.as_view(), name="delete_product"),
    
    path("categories-list/", categories.as_view(), name="categories_list"),
    path("add-category/", add_categories.as_view(), name="add_categories"),
    path("edit-category/<slug>", edit_category.as_view(), name="edit_category"),
    path("delete-category/<slug>", DeleteCategory.as_view(), name="delete_category"),
    
    path('signIn/', SignIn, name="signIn"),
    path("signUp/", SignUp , name="signup"),
    path('forget-password/', forgetPassword, name='forget_password'),
    
    
    path("customer-list/", CustomerList.as_view(), name="customer_list"),
    path("customer-info/", CustomerInfo.as_view(), name="customer_info")
]
