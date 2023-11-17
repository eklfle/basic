
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

def join(request):
    context = {"": 21}
    return render(request, "join/join.html", context)

def welcome(request):
    user_id = request.POST['user_id']
    user_pw = request.POST['user_pw']
    user_birth_date = request.POST['user_birth_date']
    user_email = request.POST['user_email']
    user_address = request.POST['user_address']
    user_tel = request.POST['user_tel']
    user_info = UserInfo(user_id = user_id, user_pw = user_pw, user_birth_date = user_birth_date,
                         user_email = user_email, user_address = user_address, user_tel = user_tel)
    user_info.save()
    user_id = {"user_id" : user_id}
    return render(request, "join/welcome.html", user_id)



