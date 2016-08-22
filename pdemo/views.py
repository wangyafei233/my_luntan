from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import MessageForm, Report, Bbs, Comment
from .forms import ExampleForm, User, Question, Answer
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
    form = User()
    if request.method == 'POST':
        form1 = User(request.POST)
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
    data = Bbs.objects.all()
    return render(request, template, {'bbs_data': data})


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
