from django.shortcuts import render

from sx_store.models import GoodsValue, ArticleCategory


# 商城首页
def index(request):
    # 首页水果展示
    if request.method == 'GET':
        fresh_fruit = GoodsValue.objects.filter(gtype_id=1, isDelete=0)[0:4]
        seafood_aquaculture = GoodsValue.objects.filter(gtype_id=2, isDelete=0)[0:4]
        red_meat = GoodsValue.objects.filter(gtype_id=3, isDelete=0)[0:4]
        poultry_egg = GoodsValue.objects.filter(gtype_id=4, isDelete=0)[0:4]
        green_goods = GoodsValue.objects.filter(gtype_id=5, isDelete=0)[0:4]
        quick_frozen = GoodsValue.objects.filter(gtype_id=6, isDelete=0)[0:4]

        data = {
            'fresh_fruit': fresh_fruit,
            'seafood_aquaculture': seafood_aquaculture,
            'red_meat': red_meat,
            'poultry_egg': poultry_egg,
            'green_goods': green_goods,
            'quick_frozen': quick_frozen,
        }
        return render(request, 'index.html', data)


# 商品列表
def list(request):
    if request.method == 'GET':
        kinds = ArticleCategory.objects.all()
        goods = GoodsValue.objects.filter(isDelete=0)
        # 商品推荐前2名
        tj_goods = GoodsValue.objects.filter(isDelete=0)[5:8]
        data = {
            'kinds': kinds,
            'goods': goods,
            'tj_goods': tj_goods
        }
        return render(request, 'list.html', data)

