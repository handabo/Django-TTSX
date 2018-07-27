from datetime import datetime, timedelta

from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from sx_store.models import GoodsValue
from sx_user.models import UserModel, UserTicketModel
from utils.functions import get_ticket


# 后台登陆
def admin_login(request):
    if request.method == 'GET':
        return render(request, 'admin/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = {}
        # 验证信息是否填写完整
        if not all([username, password]):
            data['msg'] = '用户名或者密码不能为空'
        # 验证用户是否注册
        if UserModel.objects.filter(username=username).exists():
            user = UserModel.objects.get(username=username)
            # 验证密码是否正确
            if check_password(password, user.password):
                # 如果密码正确将ticket值保存在cookie中
                ticket = get_ticket()
                response = HttpResponseRedirect(reverse('admin:admin_index'))
                out_time = datetime.now() + timedelta(days=1)
                response.set_cookie('ticket', ticket, expires=out_time)
                # 保存ticket值到数据库user_ticket表中
                UserTicketModel.objects.create(user=user,
                                               out_time=out_time,
                                               ticket=ticket)

                return response
            else:
                msg = '用户名或密码错误'
                return render(request, 'user/login.html', {'msg': msg})
        else:
            msg = '用户名不存在,请注册后在登陆'
            return render(request, 'user/login.html', {'msg': msg})


# 后台首页
def admin_index(request):
    if request.method == 'GET':
        return render(request, 'admin/index.html')


# 商品列表
def admin_product_list(request):
    if request.method == 'GET':
        goods = GoodsValue.objects.all()
        data = {
            'goods': goods
        }
        return render(request, 'admin/product_list.html', data)


# 商品详情
def admin_product_detail(request):
    if request.method == 'GET':
        return render(request, 'admin/product_detail.html')
    if request.method == 'POST':
        g_name = request.POST.get('g_name')
        g_img = request.FILES.get('g_img')
        g_num = request.POST.get('g_num')
        g_price = request.POST.get('g_price')
        g_unit = request.POST.get('g_unit')
        g_repertory = request.POST.get('g_repertory')

        if not all([g_name, g_img, g_num, g_price, g_unit, g_repertory]):
            data = {
                'msg': '商品信息请填写完整'
            }
            return render(request, 'admin/product_detail.html', data)
        # 添加商品到数据库sx_goods表中
        GoodsValue.objects.create(g_name=g_name,
                                  g_img=g_img,
                                  g_num=g_num,
                                  g_price=g_price,
                                  g_unit=g_unit,
                                  g_repertory=g_repertory,
                                  )
        # 商品添加成功后跳转到商品列表页
        return HttpResponseRedirect(reverse('admin:admin_product_list'))


# 商品回收站
def admin_recycle_bin(request):
    if request.method == 'GET':
        return render(request, 'admin/recycle_bin.html')


# 订单列表
def admin_order_list(request):
    if request.method == 'GET':
        return render(request, 'admin/order_list.html')


# 订单详情
def admin_order_detail(request):
    if request.method == 'GET':
        return render(request, 'admin/order_detail.html')


# 会员列表
def admin_user_list(request):
    if request.method == 'GET':
        return render(request, 'admin/user_list.html')


# 添加会员
def admin_user_detail(request):
    if request.method == 'GET':
        return render(request, 'admin/user_detail.html')


# 会员等级
def admin_user_rank(request):
    if request.method == 'GET':
        return render(request, 'admin/user_rank.html')


# 会员资金管理
def admin_adjust_funding(request):
    if request.method == 'GET':
        return render(request, 'admin/adjust_funding.html')


# 站点基础设置
def admin_setting(request):
    if request.method == 'GET':
        return render(request, 'admin/setting.html')


# 配送方式
def admin_express_list(request):
    if request.method == 'GET':
        return render(request, 'admin/express_list.html')


# 支付方式
def admin_pay_list(request):
    if request.method == 'GET':
        return render(request, 'admin/pay_list.html')


# 流量统计
def admin_discharge_statistic(request):
    if request.method == 'GET':
        return render(request, 'admin/discharge_statistic.html')


# 销售额统计
def admin_sales_volume(request):
    if request.method == 'GET':
        return render(request, 'admin/sales_volume.html')



