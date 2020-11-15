from django.db import models
from django.contrib.auth.models import User

class UserVip(models.Model):

    #phone_no = models.CharField(max_length=20)
    #profile_pic = models.ImageField(upload_to='images')
    user = models.OneToOneField(User, related_name='vip_user',on_delete=models.CASCADE)


class UserRegular(models.Model):

    #phone_no = models.CharField(max_length=20)
    #profile_pic = models.ImageField(upload_to='images')
    user = models.OneToOneField(User, related_name='regular_user',on_delete=models.CASCADE)


class Post(models.Model):

    text = models.CharField(max_length=256, blank=False, default='')
    V_user = models.ForeignKey(UserVip, related_name='posts', on_delete=models.CASCADE, null=True)




