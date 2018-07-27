from django.conf.urls import url

from sx_shopping import views

urlpatterns = [
    # 商品详情
    url(r'^detail/', views.detail, name='detail'),
    # 购物车
    url(r'^cart/', views.cart, name='cart'),
]

