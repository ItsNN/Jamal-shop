from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('order/history/', views.OrderHistoryView.as_view(), name='order_history')
]