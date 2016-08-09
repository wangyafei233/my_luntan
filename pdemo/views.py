from django.core.urlresolvers import reverse
from django.shortcuts import render

# Create your views here.
from .models import MessageForm, Report, Bbs
from .forms import ExampleForm, User, Question


def root_view(request, template='pdemo/boot_index.html'):
    form = ExampleForm()
    if request.method == 'POST':
        form1 = Question(request.POST)
        if form1.is_valid():
            form1.save()

    return render(request, template, {'form': form})


def adc_view(request, template='pdemo/pdemo_index.html'):
    form = MessageForm()

    return render(request, template, {'form': form})


from datetime import *


def user_view(request, template='pdemo/user_save.html'):
    form = User()
    if request.method == 'POST':
        form1 = User(request.POST)
        # form.data['end_time'] = datetime.today()
        if form.is_valid():
            form1.save()

    return render(request, template, {'form': form})
