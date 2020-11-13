
from django.urls import path

from home import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('product_detail/<slug:slug>', views.Product.as_view(), name='product_detail'),
    path('productList', views.ProductList.as_view(), name='ProductList'),
    path('send', views.Save_send.as_view(), name='send'),
    path('applications_send', views.applications_send.as_view(), name='applications')
]

