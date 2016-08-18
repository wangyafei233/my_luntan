from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^adc/$', views.adc_view, name='adc'),
    url(r'^$', views.question_view, name='shouye'),
    url(r'^answer/$', views.answer_view, name='answer'),
    url(r'^user/$', views.user_view, name='user'),
    url(r'^show/$', views.question_select_view, name='show'),
    url(r'^question/(?P<question_id>.*)$', views.question_answer_show,
        name='question'),
]
