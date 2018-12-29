from django.shortcuts import render


def data(request):
    return render(request, 'data.html', {})


def showdata(request):
    """展示数据库最后一条数据用户ID"""
    return render(request, 'showdata.html', {})
