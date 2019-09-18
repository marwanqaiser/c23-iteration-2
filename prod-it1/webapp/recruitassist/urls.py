
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
    url(r'^quiz.html/',views.quiz, name= 'quiz'),
    url(r'^quiz_new.html/',views.quiz_new, name= 'quiz_new'),
    url(r'^quiz_result/',views.quiz_result, name= 'quiz_result'),
    url(r'^location_choose/',views.location_choose, name= 'location_choose'),
    #url(r'^top_jobs/',views.top_jobs, name= 'top_jobs'),
    url(r'^top_jobs_without_mel/',views.top_jobs_without_mel, name= 'top_jobs_without_mel'),
#try to keep the naming same..avoids confusion

]

