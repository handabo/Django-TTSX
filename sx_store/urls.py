from django.conf.urls import url

from sx_store import views

urlpatterns = [
    # 商城首页
    url(r'^index/', views.index, name='index'),
    # 商城商品列表页
    url(r'^list/', views.list, name='list'),
]




