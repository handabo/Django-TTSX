from django.conf.urls import url

from sx_user import views

urlpatterns = [
    # 注册
    url(r'^register/', views.register, name='register'),
    # 登陆
    url(r'^login/', views.login, name='login'),
    # 退出
    url(r'^logout/', views.logout, name='logout'),
]