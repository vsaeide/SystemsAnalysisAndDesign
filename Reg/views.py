from django.shortcuts import render
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import UserVip,UserRegular,Post
from django.contrib.auth.models import User


def login(request):
    return render(request,'Reg/login.html',context={})

def signup(request):
    return render(request,'Reg/signup.html',context={})

def validate_register(request):


    print("validate data")


    username = request.POST.get('username')
    mail = request.POST.get('email')
    pwd = request.POST.get('password')
    type = request.POST.get('type')
    # confirm_pwd =request.POST.get('confirm')

    fieldvalue_dict = {}
    # fieldvalue_dict["fname"]=fname
    # fieldvalue_dict["sname"]=sname
    fieldvalue_dict["username"] = username
    fieldvalue_dict["mail"] = mail
    fieldvalue_dict["pwd"] = pwd
    fieldvalue_dict["type"] = type


    can_proceed = True
    error_message = ''

    if not username.strip() :
        can_proceed = False
        error_message = 'Please enter Username.'

    if not mail.strip():
        can_proceed = False
        error_message = 'Please enter your  Email.'

    if not pwd.strip() and can_proceed == True:
        can_proceed = False
        error_message = 'Please enter password.'

    # if not confirm_pwd.strip() and can_proceed == True:
    #     can_proceed = False
    #     error_message = 'Please confirm password.'


    if can_proceed == True :

        user_by_user_name = None
        user_by_email=None

        try:
            user_by_user_name = User.objects.get(username=username)
        except:
            can_proceed = True

        if user_by_user_name:

            can_proceed = False
            error_message = 'Username already exists.'

        if can_proceed == True:

            try:
                user_by_email = User.objects.get(email=mail)
            except:
                can_proceed = True

        if user_by_user_name:
            can_proceed = False
            error_message = 'this Email already exists.'

        if can_proceed == True:

            user = User.objects.create_user(username=username,email=mail,password=pwd)
            if type=="vip":
                user_vip = UserVip.objects.create(user =user)
                user_vip.save()
            else:
                user_regular=UserRegular.objects.create(user =user)
                user_regular.save()

    if can_proceed == True:

        return render(request,'Reg/signup.html',context={})

    else:

        return render(request,'Reg/signup.html',context={'error_message':error_message,'valuedict':fieldvalue_dict})


