from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from Reg import views as core_views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^home/', core_views.home, name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
]
