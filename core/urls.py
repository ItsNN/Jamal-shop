from django.urls import path
from django.views.generic import TemplateView
from . import  views
urlpatterns = [
    path("", views.MenuListView.as_view(),  name='menu_list'),
    path("category/<slug:category_slug>/", views.MenuListView.as_view(), name='menu_item_list_by_category'),
    path("subcategory/<slug:subcategory_slug>/", views.MenuListView.as_view(), name='menu_item_list_by_subcategory'),
    path("product-detail/<slug:slug>/", views.MenuItemDetailView.as_view(), name='menu_item_detail'),
    path('order-summary-page/', TemplateView.as_view(template_name='pages/order-summary.html')),
    path('checkout-page/', TemplateView.as_view(template_name='pages/checkout.html')),
    path('products-on-offer/', views.OfferedProductListView.as_view(), name='offer_products')
    ]