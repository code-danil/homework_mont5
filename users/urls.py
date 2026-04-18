from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('confirm/', views.ConfirmView.as_view(), name='confirm'),
    path('login/', views.AuthorizationView.as_view(), name='login'),
]

