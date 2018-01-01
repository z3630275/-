# _*_ coding:utf-8 _*_
__author__ = '111'
__date__ = '2018/1/1 17:43'
from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^pro/$',views.pro),
    url(r'^city(\d+)/$',views.city),
    url(r'^dis(\d+)/$',views.dis),

]
