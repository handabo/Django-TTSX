from django.conf.urls import url

from sx_shopping import views

urlpatterns = [
    # 商品详情
    url(r'^detail/', views.detail, name='detail'),
    # 增加商品数量
    url(r'^addgoods/', views.add_goods, name='addgoods'),
    # 减少商品数量
    url(r'^subgoods/', views.sub_goods, name='subgoods'),
    # 刷新增添与减少商品数量
    url(r'^goodsnum/', views.goods_num, name='goodsnum'),
    # 计算商品总价
    url(r'^tatalprice/', views.tatal_price, name='tatalprice'),

    # 立即购买
    url(r'^buycart/', views.buy_cart, name='buycart'),
    # 加入购物车
    url(r'^addcart/', views.add_cart, name='addcart'),
]

