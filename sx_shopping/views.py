from django.shortcuts import render


# 商品详情
def detail(request):
    if request.method == 'GET':
        return render(request, 'detail/detail.html')

# 购物车
def cart(request):
    if request.method == 'GET':
        return render(request, 'cart/cart.html')

