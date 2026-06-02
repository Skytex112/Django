from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.business_dashboard, name='business_dashboard'),
    
    path('dashboard/product/create/', views.edit_entity, {'entity_type': 'product'}, name='product_create'),
    path('dashboard/product/edit/<uuid:obj_id>/', views.edit_entity, {'entity_type': 'product'}, name='product_edit'),
    path('dashboard/product/delete/<uuid:obj_id>/', views.delete_entity, {'entity_type': 'product'}, name='product_delete'),
    
    path('dashboard/seller/create/', views.edit_entity, {'entity_type': 'seller'}, name='seller_create'),
    path('dashboard/seller/edit/<uuid:obj_id>/', views.edit_entity, {'entity_type': 'seller'}, name='seller_edit'),
    path('dashboard/seller/delete/<uuid:obj_id>/', views.delete_entity, {'entity_type': 'seller'}, name='seller_delete'),
    
    path('dashboard/client/create/', views.edit_entity, {'entity_type': 'client'}, name='client_create'),
    path('dashboard/client/edit/<uuid:obj_id>/', views.edit_entity, {'entity_type': 'client'}, name='client_edit'),
    path('dashboard/client/delete/<uuid:obj_id>/', views.delete_entity, {'entity_type': 'client'}, name='client_delete'),

    path('dashboard/sale/create/', views.edit_entity, {'entity_type': 'sale'}, name='sale_create'),
    path('dashboard/sale/edit/<uuid:obj_id>/', views.edit_entity, {'entity_type': 'sale'}, name='sale_edit'),
    path('dashboard/sale/delete/<uuid:obj_id>/', views.delete_entity, {'entity_type': 'sale'}, name='sale_delete'),
]
