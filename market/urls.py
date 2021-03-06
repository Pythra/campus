from django.urls import path
from . import views

urlpatterns = [
        path('', views.market_index, name='home'),
        path('<slug:slug>/', views.product_detail, name='product_detail'),
        path('house/<int:pk>/', views.house_detail, name='house_detail'),
        path('product/create/', views.product_create, name='product_form'),
        path('product/<slug:slug>/update/', views.ProductUpdate.as_view(), name='product_update'),
        path('product/<slug:slug>/delete/', views.ProductDelete.as_view(), name='product_confirm_delete'),
        path('service/create/', views.service_create, name='service_form'),
        path('service/<slug:slug>/', views.service_detail, name='service_detail'),
        path('service/<slug:slug>/update/', views.ServiceUpdate.as_view(), name='service_update'),
        path('service/<slug:slug>/delete/', views.ServiceDelete.as_view(), name='service_confirm_delete'),
        path('<slug:slug>/review/create/', views.review_create, name='review_form'),
        path('house/create/', views.house_create, name='house_form'),
        path('review/<int:pk>/update/', views.ReviewUpdate.as_view(), name='review_update'),
        path('review/<int:pk>/delete/', views.ReviewDelete.as_view(), name='review_confirm_delete'),
        path('my_shop/<int:pk>/restructure/', views.ShopUpdate.as_view(), name='shop_update'),
        path('my_shop/<int:pk>/close_down/', views.ServiceDelete.as_view(), name='shop_confirm_delete'),
        path('search/results/', views.search, name='search_home'),
        path('my_shop/details/', views.my_shop, name='my_shop'),
        path('shop/visit/<int:pk>/', views.visit_shop, name='visit_shop'),
        path('request/<int:pk>/', views.request_detail, name='request_detail'),
        path('request/create/form/', views.request_create, name='request_form'),
        path('all_items/my_area/', views.all_products, name='all_area_products'),  
        path('all_services/my_school/', views.all_services, name='all_services'),
        path('all_shops/my_area/', views.all_shops, name='all_shops'),
        path('settings/options/', views.settings, name='settings'),
                ]
