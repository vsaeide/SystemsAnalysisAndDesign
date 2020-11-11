from django.urls import path
from .views import home,register_page,validate_register,userprofile_page

urlpatterns = [
    path('home',home,name='home'),
    path('register',register_page,name='Register'),
    path('valreg',validate_register,name='validate_register'),
    path('userprofile',userprofile_page,name='user_profile'),
]