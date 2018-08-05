from django.http import JsonResponse
from django.shortcuts import render

from sx_shopping.models import CartInfo
from sx_store.models import GoodsValue, ArticleCategory


# 商品详情
def detail(request):
    if request.method == 'GET':
        kinds = ArticleCategory.objects.all()
        # 拿到的详情商品
        g_id = request.GET.get('g_id')
        goods = GoodsValue.objects.filter(id=g_id).first()

        # 拿到的新品推荐商品
        # pass

        data = {
            'kinds': kinds,
            'goods': goods
        }
        return render(request, 'detail.html', data)


# 增加商品数量
def add_goods(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        data['code'] = '1000'
        data['msg'] = '请登录后再使用'

        if user.id:
            goods_id = request.POST.get('goods_id')
            # 验证当前登录用户是否对同一商品进行添加操作, 如果有则继续添加
            cart = CartInfo.objects.filter(user=user, goods_id=goods_id).first()
            if cart:
                cart.count += 1
                cart.save()
                data['count'] = cart.count
            else:
                # 验证当前登陆用户有没有添加商品到购物车中，如果没有则创建
                CartInfo.objects.create(user=user, goods_id=goods_id)
                data['count'] = 1
            data['code'] = '200'
            data['msg'] = '请求成功'
            return JsonResponse(data)
        return JsonResponse(data)


# 减少商品数量
def sub_goods(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        data['code'] = '1000'
        data['msg'] = '请登录后再使用'
        if user.id:
            goods_id = request.POST.get('goods_id')
            cart = CartInfo.objects.filter(user=user, goods_id=goods_id).first()
            if cart:
                if cart.count == 1:
                    cart.delete()
                    data['count'] = 0
                else:
                    cart.count -= 1
                    cart.save()
                    data['count'] = cart.count
                data['code'] = '200'
                data['msg'] = '请求成功'
                return JsonResponse(data)
            else:
                data['msg'] = '请添加商品'
                return JsonResponse
        else:
            return JsonResponse


# 刷新增添与减少商品数量
def goods_num():
    pass



# 立即购买
def buy_cart(request):
    if request.method == 'GET':
        return render(request, 'cart.html')


# 加入购物车
def add_cart(request):
    pass

