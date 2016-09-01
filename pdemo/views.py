#!/usr/bin/python
# coding:utf-8
from authtools.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import MessageForm, Report, Bbs, Comment, ExampleModel
from .forms import ExampleForm, Question, Answer, ImageUploadForm, \
    ViewActionForm
from .forms import User as User1
from authtools.views import LoginRequiredMixin


@login_required()
def answer_view(request, template='pdemo/answer.html'):
    form = Answer()
    if request.method == 'POST':
        form = Answer(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/answer')

    return render(request, template, {'form': form})


@login_required()
def adc_view(request, template='pdemo/z_adc.html'):
    form = MessageForm()

    return render(request, template, {'form': form})


@login_required()
def user_view(request, template='pdemo/z_user_save.html'):
    form = User1()
    if request.method == 'POST':
        form1 = User1(request.POST)
        # form.data['end_time'] = datetime.today()
        if form.is_valid():
            form1.save()

    return render(request, template, {'form': form})


@login_required()
def question_view(request, template='pdemo/index.html'):
    form = ExampleForm()
    form_erro = ''
    if request.method == 'POST':
        form1 = Question(request.POST)
        if form1.is_valid():
            form1.save()
            form_erro = 'ok'
        else:
            form_erro = 'shuru youwu'

    return render(request, template, {'form': form, 'erro': form_erro})


@login_required()
def question_select_view(request, template='pdemo/question_show.html'):
    form = ViewActionForm()
    data = None
    search_args = []
    if request.method == 'POST':
        form1 = ViewActionForm(request.POST)
        if form1.is_valid():
            title = form1.cleaned_data['title']
            authon = form1.cleaned_data['author_z']
            if title: search_args.append(Q(QuestionTitle__contains=title))
            if authon: search_args.append(
                Q(QuestionAuthor__name__exact=authon))
            data = Bbs.objects.filter(*search_args)
            # data = Bbs.objects.filter(QuestionTitle__contains=title).filter(
            #     QuestionAuthor=user_id)
            # user_id = User.objects.filter(name=authon)
            # q = {'QuestionTitle__contains': title} #add q['key']='value'

    return render(request, template, {'bbs_data': data, 'form': form})


@login_required()
def question_answer_show(request, question_id,
                         template='pdemo/question_answer_show.html'):
    if request.method == 'POST':
        form = Answer(request.POST)
        if form.is_valid():
            form.save()
    question_data = Bbs.objects.filter(id=question_id).first()
    answer_data = question_data.comment_set.all()
    return render(request, template,
                  {'bbs_data': question_data, 'answer_data': answer_data})


# 上传图片
def upload_pic(request, template='pdemo/img_up.html'):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)  # 有文件上传要传如两个字段
        if form.is_valid():
            m = ExampleModel()
            m.model_pic = form.cleaned_data['image']  # 直接在这里使用 字段名获取即可
            m.save()
            return HttpResponseRedirect('/img')
            # 删除记录
            #     m = ExampleModel.objects.get(pk=1)
            # os.remove(m.model_pic.name)
            # m.delete()

    return render(request, template, {'img': ExampleModel.objects.all()})
