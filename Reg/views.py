from django.shortcuts import render
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import UserProfile
from django.contrib.auth.models import User

def home(request):
    return render(request,'Reg/home.html',context={})

def register_page(request):
    return render(request,'Reg/Register.html',context={})

def validate_register(request):

    fname = request.POST.get('firstname')
    sname = request.POST.get('secondname')
    mail = request.POST.get('email')
    contact = request.POST.get('contact')
    username = request.POST.get('username')
    pwd = request.POST.get('password')
    confirm_pwd =request.POST.get('confirm')

    fieldvalue_dict = {}
    fieldvalue_dict["fname"]=fname
    fieldvalue_dict["sname"]=sname
    fieldvalue_dict["mail"] = mail
    fieldvalue_dict["contact"] = contact
    fieldvalue_dict["username"] = username
    fieldvalue_dict["pwd"] = pwd



    can_proceed = True
    error_message = ''

    if not fname.strip():
        can_proceed = False
        error_message = 'Please enter  first name.'
    if not sname.strip() and can_proceed == True:
        can_proceed = False
        error_message = 'Please enter  second name.'

    if not mail.strip() and can_proceed == True:
        can_proceed = False
        error_message = 'Please enter Emailid.'

    if not contact.strip() and can_proceed == True:
        can_proceed = False
        error_message = 'Please enter contact number.'

    if not username.strip() and can_proceed == True:
        can_proceed = False
        error_message = 'Please enter Username.'

    if not pwd.strip() and can_proceed == True:
        can_proceed = False
        error_message = 'Please enter password.'

    if not confirm_pwd.strip() and can_proceed == True:
        can_proceed = False
        error_message = 'Please confirm password.'

    profile_picture = request.FILES

    print(profile_picture)

    if 'profile_pic' in profile_picture.keys():
        print('profile pic exists.')

    else:
        print('no pic.')
        profile_picture = None
        can_proceed = False

    if can_proceed == True :

        user_by_user_name = None
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
                error_message = 'Email id already exists.'

        if can_proceed == True:

            pic = request.FILES['profile_pic']

            user = User.objects.create_user(username=username,email=mail,password=pwd,first_name=fname,last_name=sname)
            user_profile = UserProfile.objects.create(phone_no=contact, profile_pic= pic,user =user)

    if can_proceed == True:

        return render(request,'Reg/home.html',context={})

    else:

        return render(request,'Reg/Register.html',context={'error_message':error_message,'valuedict':fieldvalue_dict})


def userprofile_page(request):

    pic_url = request.user.user_profile.profile_pic

    return render(request,'Reg/userprofile.html',context={'image_url':pic_url})