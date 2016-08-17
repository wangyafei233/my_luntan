from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import MessageForm, Report, Bbs
from .forms import ExampleForm, User, Question, Answer
from authtools.views import LoginRequiredMixin


def question_view(request, template='pdemo/index.html'):
    form = ExampleForm()
    form_erro = ''
    if request.method == 'POST':
        form1 = Question(request.POST)
        if form1.is_valid():
            form1.save()
        else:
            form_erro = 'shuru youwu'

    return render(request, template, {'form': form, 'erro': form_erro})


def answer_view(request, template='pdemo/answer.html'):
    form = Answer()
    if request.method == 'POST':
        form = Answer(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/answer')

    return render(request, template, {'form': form})


def adc_view(request, template='pdemo/adc.html'):
    form = MessageForm()

    return render(request, template, {'form': form})


def user_view(request, template='pdemo/user_save.html'):
    form = User()
    if request.method == 'POST':
        form1 = User(request.POST)
        # form.data['end_time'] = datetime.today()
        if form.is_valid():
            form1.save()

    return render(request, template, {'form': form})
