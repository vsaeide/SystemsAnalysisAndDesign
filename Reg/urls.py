from django.urls import path
from .views import validate_register,login,signup

urlpatterns = [
    path('login/',login,name='home'),
    path('register/',validate_register,name='Register'),
    path('signup/', signup, name='signup'),
    #path('validate/',validate_register,name='validate_register'),
    #path('validate/', validate_register, name='validate_register'),
    #path('userprofile',userprofile_page,name='user_profile'),
]