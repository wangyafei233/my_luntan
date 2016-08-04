from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response

# Create your views here.
from .models import MessageForm, Report
from .forms import ExampleForm


def root_view(request, template='pdemo/boot_index.html'):
    form = ExampleForm()

    return render(request, template, {'form': form})


def adc_view(request, template='pdemo/pdemo_index.html'):
    form = MessageForm()

    return render(request, template, {'form': form})
