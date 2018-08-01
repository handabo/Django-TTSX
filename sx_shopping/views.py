from django.shortcuts import render

from sx_store.models import GoodsValue, ArticleCategory


# 商品详情
def detail(request):
    if request.method == 'GET':
        kinds = ArticleCategory.objects.all()
        g_id = request.GET.get('g_id')
        goods = GoodsValue.objects.filter(id=g_id).first()
        data = {
            'kinds': kinds,
            'goods': goods
        }
        return render(request, 'detail.html', data)


# 购物车
def cart(request):
    if request.method == 'GET':
        return render(request, 'cart.html')

