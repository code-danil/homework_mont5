from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:id>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('products/', views.ProductsListView.as_view(), name='product-list'),
    path('products/<int:id>/', views.ProductsDetailView.as_view(), name='product-detail'),
    path('reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:id>/', views.ReviewDetailView.as_view(), name='review-detail'),
]