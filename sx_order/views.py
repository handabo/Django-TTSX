from django.shortcuts import render

from sx_shopping.models import CartInfo


# 提交订单
def place_order(request):
    if request.method == 'GET':
        user = request.user
        carts = CartInfo.objects.filter(user=user)
        data = {'carts': carts}
        return render(request, 'place_order.html', data)


