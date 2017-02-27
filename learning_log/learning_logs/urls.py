# Defines URL patterns for learning_logs
from django.conf.urls import url
from . import views

urlpatters=[
    #Home Page
    url(r'^$', views.index, name='index'),

    #Show all topics
    url(r'^topics/$', views.topics, name='topics'),

    #Page for individual topic
    url(r'^topics/(?P<topic_id>\d+)$', views.topic, name='topic'),
]
