from django.conf.urls import url

from sx_user import views

urlpatterns = [
    # 注册
    url(r'^register/', views.register, name='register'),
    # 登陆
    url(r'^login/', views.login, name='login'),
    # 用户中心 - 用户信息页
    url(r'^user_center_info/', views.user_center_info, name='user_center_info'),
    # 用户中心 - 用户订单页
    url(r'^user_center_order/', views.user_center_order, name='user_center_order'),
    # 用户中心 - 用户收货地址页
    url(r'^user_center_site/', views.user_center_site, name='user_center_site'),
]