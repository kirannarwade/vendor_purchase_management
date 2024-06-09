from django.urls import path
from .import views

urlpatterns = [
    path('vendors/', views.VendorList_Create.as_view(), name='vendors_create'),
    path('vendors/<int:id>/', views.VenderInfo.as_view(), name='vendor_list'),

    path('purchase_orders/', views.PurchaseOrderList_Create.as_view(), name='purchase_orders_create'),
    path('purchase_orders/<int:id>/', views.PurchaseOrderInfo.as_view(), name='purchase_orders_list'),

    path('vendors/<int:pk>/performance/', views.VendorPerformanceView.as_view(), name='vendor-performance'),

]
