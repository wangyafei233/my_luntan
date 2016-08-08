from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^adc/', views.adc_view, name='adc'),
    url(r'^$', views.root_view, name='shouye'),
    url(r'^user/', views.user_view, name='user'),
]
