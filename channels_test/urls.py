from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.about, name='about'),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^room-(?P<label>[\w-]{0,50})/$', views.chat_room, name='chat_room'),
    url(r'^demo11/$', views.demo, name='demo11'),

]
