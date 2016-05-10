from django.conf.urls import url
from django.contrib import admin
from . import views as v

urlpatterns = [
    url(r'^create$', v.post_create),
    url(r'^detail$', v.post_detail),
    url(r'^$', v.post_list),
    url(r'^update$', v.post_update),
    url(r'^delete$', v.post_delete),
]