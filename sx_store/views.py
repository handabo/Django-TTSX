from django.shortcuts import render


# 商城首页
def index(request):
    if request.method == 'GET':
        return render(request, 'home/index.html')

# 商品列表
def list(request):
    if request.method == 'GET':
        return render(request, 'list/list.html')

