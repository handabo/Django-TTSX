from django.shortcuts import render


# 提交订单
def place_order(request):
    if request.method == 'GET':
        return render(request, 'place_order/place_order.html')


