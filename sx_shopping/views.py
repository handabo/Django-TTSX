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
        if user.id:
            goods_id = request.POST.get('goods_id')
            # 验证当前登录用户是否对同一商品进行添加操作, 如果有则继续添加
            cart = CartInfo.objects.filter(user=user, goods_id=goods_id).first()
            if cart:
                cart.count += 1
                cart.save()
                data['count'] = cart.count
                # 计算单个商品总价
                data['goods_price'] = round(cart.goods.g_price * cart.count, 2)
            else:
                # 验证当前登陆用户有没有添加商品到购物车中，如果没有则创建
                CartInfo.objects.create(user=user, goods_id=goods_id)
                data['count'] = 1
            data['code'] = '200'
            data['msg'] = '请求成功'
            return JsonResponse(data)
        data['code'] = '1000'
        data['msg'] = '请登录后再使用'
        return JsonResponse(data)


# 减少商品数量
def sub_goods(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        if user.id:
            goods_id = request.POST.get('goods_id')
            cart = CartInfo.objects.filter(user=user, goods_id=goods_id).first()
            if cart:
                if cart.count == 1:
                    # cart.delete()
                    # data['count'] = 0
                    data['msg'] = '亲! 至少买一个吧'
                else:
                    cart.count -= 1
                    cart.save()
                    data['count'] = cart.count
                    # 计算单个商品总价
                    data['goods_price'] = round(cart.goods.g_price * cart.count, 2)
                data['code'] = '200'
                data['msg'] = '请求成功'
                return JsonResponse(data)
            else:
                data['msg'] = '请添加商品'
                return JsonResponse(data)
        else:
            data['code'] = '1001'
            data['msg'] = '请登录后再使用'
            return JsonResponse(data)


# 刷新商品增添/减少数量, 单个商品总价刷新
def goods_num(request):
    if request.method == 'GET':
        user = request.user
        cart_list = []
        if user.id:
            carts = CartInfo.objects.filter(user=user)
            for cart in carts:
                data = {
                    'id': cart.id,
                    'goods_id': cart.goods.id,
                    'count': cart.count,
                    'user_id': cart.user.id,
                    # 单个商品总价
                    'goods_price': round(cart.goods.g_price * cart.count, 2)
                }
                cart_list.append(data)
            data = {
                'carts': cart_list,
                'code': '200',
                'msg': '请求成功'
            }
            return JsonResponse(data)
        else:
            data = {
                'carts': '',
                'code': '1002',
                'msg': '请登录后再使用'
            }
            return JsonResponse(data)


# 加入购物车
def add_cart(request):
    if request.method == 'POST':
        user = request.user
        carts = CartInfo.objects.filter(user=user)
        pass


# 立即购买
def buy_cart(request):
    if request.method == 'GET':
        user = request.user
        carts = CartInfo.objects.filter(user=user)
        data = {'carts': carts}
        return render(request, 'cart.html', data)


# 计算商品总价
def tatal_price(request):
    if request.method == 'GET':
        user = request.user
        # 获取购物车中的商品信息
        carts = CartInfo.objects.filter(user=user)
        tatal_price = 0
        num = 0
        for cart in carts:
            tatal_price += cart.goods.g_price * cart.count
            # 计算购物车商品件数
            num += 1
        # 总价保留2位小数
        tatal_price = round(tatal_price, 2)
        data = {
            'tatal_price': tatal_price,
            'num': num,
            'code': '200',
            'msg': '请求成功'
        }
        return JsonResponse(data)




