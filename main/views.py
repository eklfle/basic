from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from inventory.models import *
from django.template import loader

def main(request):
    # 메인 페이지
    inventory_item_list = Inventory.objects.order_by('product_name')
    itemlist = []
    for item in inventory_item_list:
        if item.product_name in itemlist:
            pass
        else:
            itemlist.append(item.product_name)

    if 'user_id' in request.session.keys():
        # return HttpResponse("로그인 성공~~~ 메인페이지")
        print(request.session.keys())
        user_id = request.session.get('user_id')
        context = {"user_id" : user_id, 'inventory_item_list' : itemlist}
        return render(request, "main/main.html", context)
    else:
        context = {"user_id": "", 'inventory_item_list' : itemlist}
        return render(request, "main/main.html", context)

def logout(request):
    # return HttpResponse("로그아웃 시도")
    del request.session['user_id']
    return redirect("main")

def category(request, category):
    category_list = Inventory.objects.filter(category=category)
    itemlist = []
    for item in category_list:
        if item.product_name in itemlist:
            pass
        else:
            itemlist.append(item.product_name)

    if 'user_id' in request.session.keys():
        user_id = request.session.get('user_id')
        context = {"category_list" : itemlist, "user_id" : user_id}
    else:
        context = {"category_list" : itemlist, "user_id" : ""}

    return render(request, "main/category.html", context)

def mypage(request):
    if 'user_id' in request.session.keys():
        user_id = request.session.get('user_id')
        context = {"user_id" : user_id}
        return render(request, "main/mypage.html", context)
    else:
        return HttpResponse("로그인 하지 않은 유저입니다.")

def cart(request, order_list):
    user_id = request.session.get('user_id')

    print("orderlist : ", order_list)
    print(list(request.POST.items()))

    order_list = request.POST['entire_order_list']
    print(order_list)

    if request.method == 'POST':
        print(request.POST)
        for key, value in request.POST.items():
            print("키 : ", key)
            print("값 : ", value)

    return HttpResponse("장바구니 페이지")

def detail(request, product_name):
    product_info = Inventory.objects.filter(product_name = product_name)
    for item in product_info:
        print(item.color)

    context = {"product_info" : product_info, "product_name":product_name}
    return render(request, "main/detail.html", context)

def best(request):
    return HttpResponse("베스트 페이지 입니다.")

def search(request):
    search_keyword = request.GET['search_txt_box']
    print(search_keyword)
    product_name_search_result = Inventory.objects.filter(product_name = search_keyword)
    category_search_result = Inventory.objects.filter(category=search_keyword)
    product_id_search_result = Inventory.objects.filter(product_id=search_keyword)
    color_search_result = Inventory.objects.filter(color=search_keyword)
    context = {
        "search_keyword" : search_keyword,
        "product_name_search_result" : product_name_search_result,
        "category_search_result": category_search_result,
        "product_id_search_result": product_id_search_result,
        "color_search_result": color_search_result,
    }
    return render(request, "main/search.html", context)



