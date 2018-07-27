from django.conf.urls import url

from sx_order import views

urlpatterns = [
    # 提交订单
    url(r'^place_order/', views.place_order, name='place_order'),
]

