from django.urls import path

from new_app import views, customer_views, seller_views, admin_views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('userlogin',views.profilelogin,name='userlogin'),
    path('customer_reg',customer_views.customer_reg,name='customer_reg'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('sellerpage',views.sellerpage,name='sellerpage'),
    path('customerpage',views.customerpage,name='customerpage'),
    path('seller_reg',seller_views.seller_reg,name='seller_reg'),
    path('seller_list',admin_views.seller_list,name='seller_list'),
    path('add_products',seller_views.add_product,name='add_products'),
    path('product_view',seller_views.product_view,name='product_view'),
    path('product_delete<int:id>/',seller_views.product_delete,name='product_delete'),
    path('product_update<int:id>/',seller_views.product_update,name='product_update'),
    path('admin_product_view',admin_views.admin_product_view,name='admin_product_view'),
    path('cust_product_view',customer_views.cust_product_view,name='cust_product_view'),
    path('add_to_cart<int:id>/',customer_views.add_to_cart,name='add_to_cart'),
    path('view_cart',customer_views.view_cart,name='view_cart'),
    path('remove_from_cart<int:id>/',customer_views.remove_from_cart,name='remove_from_cart'),
    path('customer_details<int:id>/',customer_views.customer_details,name='customer_details'),
    path('customer_payment<int:id>/',customer_views.customer_payment,name='customer_payment'),
    path('customer_orders',customer_views.customer_orders,name='customer_orders'),
    path('cancel_order<int:id>/',customer_views.cancel_order,name='cancel_order'),
    path('seller_orders',seller_views.seller_orders,name='seller_orders'),
    path('admin_orders',admin_views.admin_orders,name='admin_orders'),
]


