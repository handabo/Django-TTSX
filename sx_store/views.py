from django.shortcuts import render


def index(request):
    if request.method == 'GET':
        return render(request, 'home/index.html')


def list(request):
    if request.method == 'GET':
        return render(request, 'list/list.html')

