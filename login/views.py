from join.models import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
def login(request):
    context = {"":''}
    return render(request, "login/login.html", context)

def login_try(request):
    login_try_user_id = request.POST['user_id']
    login_try_user_pw = request.POST['user_pw']

    try:
        login_try_user_info = UserInfo.objects.get(user_id=login_try_user_id)
    except UserInfo.DoesNotExist:
        return HttpResponseRedirect(reverse("login"))

    if login_try_user_info.user_pw == login_try_user_pw:
        request.session["user_id"] = login_try_user_id
        return HttpResponseRedirect(reverse("main"), )
    else:
        return HttpResponseRedirect(reverse("login"))












