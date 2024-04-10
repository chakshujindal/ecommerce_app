from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    # Add other URL patterns as needed
]
