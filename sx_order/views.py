from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from sx_shopping.models import CartInfo
from sx_user.models import UserModel


# 提交订单
def place_order(request):
    if request.method == 'GET':
        user = request.user
        carts = CartInfo.objects.filter(user=user)
        data = {'carts': carts}
        return render(request, 'place_order.html', data)


# 个人信息
def user_center_info(request):
    if request.method == 'GET':
        return render(request, 'user_center_info.html')


# 全部订单
def user_center_order(request):
    if request.method == 'GET':
        return render(request, 'user_center_order.html')


# 收货地址
def user_center_site(request):
    # 拿到登陆用户的id
    id = request.user.id
    user_info = UserModel.objects.filter(id=id).first()
    if request.method == 'GET':
        data = {'user_info': user_info}
        return render(request, 'user_center_site.html', data)

    if request.method == 'POST':
        recipients = request.POST.get('recipients')
        direction = request.POST.get('direction')
        addressee_p = request.POST.get('addressee_p')
        phone = request.POST.get('phone')
        # 验证信息是否填写完整
        if not all([recipients, direction, addressee_p, phone]):
            data = {'msg': '请填写完整的收货信息!',
                    'user_info': user_info}  # 避免提交表单信息为空时当前地址不显示
            return render(request, 'user_center_site.html', data)
        user_info.recipients=recipients
        user_info.direction=direction
        user_info.addressee_p=addressee_p
        user_info.phone=phone
        user_info.save()
        data = {'msg': '收货地址添加成功'}
        return HttpResponseRedirect(reverse('order:user_center_site'), data)




