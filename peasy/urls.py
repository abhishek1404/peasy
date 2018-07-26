"""peasy URL Configuration
"""
from django.conf.urls import  url
from django.contrib import admin
from approval.views import user_page,approve,signup,ask_approval
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login,{'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', lambda request: logout_then_login(request, "/login"), name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^home/',user_page, name='user-page'),
    url(r'^approve/', approve, name='approve'),
    url(r'^ask_approval/', ask_approval, name='ask-approval'),
]
