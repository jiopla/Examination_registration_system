from django.contrib.auth.views import login
from django.conf.urls import url
from django.conf import settings
from . import views

app_name='users'
urlpatterns = [
    url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^register/$',views.register,name='register'),
    # url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
]