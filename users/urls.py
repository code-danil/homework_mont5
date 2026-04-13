from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('confirm/', views.confirm_view, name='confirm'),
    path('login/', views.authorzation_view, name='login'),
]