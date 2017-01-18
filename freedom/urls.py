from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.freedom_index_view, name='freedom'),
    url(r'^qipao/', views.freedom_pao_view, name='qipao'),

]
