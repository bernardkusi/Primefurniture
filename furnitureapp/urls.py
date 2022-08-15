from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('products',views.products,name='products'),
    path('cart',views.cart,name='cart'),
    path('products/<str:pk>/',views.product,name='product'),
    path('purchase/<str:pk>/',views.purchases,name='purchase'),
    path('remove/',views.remove,name='remove'),
    path('order/',views.order,name='order'),
    path('message/',views.message,name='message'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('signout/',views.signout,name='signout'),
]
