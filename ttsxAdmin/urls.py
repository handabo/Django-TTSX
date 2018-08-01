from django.conf.urls import url

from ttsxAdmin import views

urlpatterns = [
    # 后台登陆
    url(r'^admin_login/', views.admin_login, name='admin_login'),
    # 后台首页
    url(r'^admin_index/', views.admin_index, name='admin_index'),
    # 商品列表分页展示
    url(r'^admin_product_list/', views.admin_product_list, name='admin_product_list'),
    # 添加商品
    url(r'^admin_product_detail/', views.admin_product_detail, name='admin_product_detail'),
    # 修改商品
    url(r'^admin_change_goods/', views.admin_change_goods, name='admin_change_goods'),
    # 删除商品
    url(r'^admin_del_goods/', views.admin_del_goods, name='admin_del_goods'),
    # 商品回收站
    url(r'^admin_recycle_bin/', views.admin_recycle_bin, name='admin_recycle_bin'),
    # 恢复商品
    url(r'^admin_recover_goods/', views.admin_recover_goods, name='admin_recover_goods'),
    # 彻底删除商品
    url(r'^admin_delete_goods/', views.admin_delete_goods, name='admin_delete_goods'),


    # 查找商品
    url(r'^admin_find_goods/', views.admin_find_goods, name='admin_find_goods'),
    # 订单列表
    url(r'^admin_order_list/', views.admin_order_list, name='admin_order_list'),
    # 订单详情
    url(r'^admin_order_detail/', views.admin_order_detail, name='admin_order_detail'),
    # 会员列表
    url(r'^admin_user_list/', views.admin_user_list, name='admin_user_list'),
    # 添加会员
    url(r'^admin_user_detail/', views.admin_user_detail, name='admin_user_detail'),
    # 会员等级
    url(r'^admin_user_rank/', views.admin_user_rank, name='admin_user_rank'),
    # 会员资金管理
    url(r'^admin_adjust_funding/', views.admin_adjust_funding, name='admin_adjust_funding'),
    # 站点基础设置
    url(r'^admin_setting/', views.admin_setting, name='admin_setting'),
    # 配送方式
    url(r'^admin_express_list/', views.admin_express_list, name='admin_express_list'),
    # 支付方式
    url(r'^admin_pay_list/', views.admin_pay_list, name='admin_pay_list'),
    # 流量统计
    url(r'^admin_discharge_statistic/', views.admin_discharge_statistic, name='admin_discharge_statistic'),
    # 销售额统计
    url(r'^admin_sales_volume/', views.admin_sales_volume, name='admin_sales_volume'),
]

