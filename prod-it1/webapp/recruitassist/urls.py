
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # ^ is start and $ is end---looks in views file for index method
    url(r'^SeekSuburb-index.html',views.seek, name= 'seek'),
    url(r'^Homepage-IE.html',views.home, name= 'home'),
    url(r'^ShowService.html',views.service, name= 'service'),
    url(r'^about_us.html',views.about_us, name= 'about_us'),
    url(r'^listprovider/',views.listprovider, name= 'listprovider'),



]

