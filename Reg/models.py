from django.db import models
from django.contrib.auth.models import User

# ****************************************************************************************
# ****************************************************************************************
# To store user profile details with reference to the Django user
# ****************************************************************************************
# ****************************************************************************************

class UserProfile(models.Model):

    phone_no = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='images')
    user = models.OneToOneField(User, related_name='user_profile',on_delete=models.CASCADE)


