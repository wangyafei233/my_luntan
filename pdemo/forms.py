#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime

from crispy_forms.bootstrap import FormActions, AppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Field, Div, \
    ButtonHolder, HTML, Reset, Button
from django import forms
from django.core.urlresolvers import reverse
from django.forms import TimeField, IntegerField, Textarea, CharField
from django.utils.translation import ugettext as _
from .models import Report, Bbs, Comment


class ExampleForm(forms.Form):
    QuestionTime = forms.DateTimeField(
        label="QuestionTime",
        required=False,
        initial=datetime.today()
    )

    QuestionAuthor = forms.CharField(
        label="QuestionAuthor?",
        max_length=255,
    )

    QuestionTitle = forms.CharField(
        label="QuestionTitle?",
        max_length=255,
        required=True,
    )

    QuestionSupply = forms.CharField(
        label="QuestionSupply",
        max_length=1000,
    )

    QuestionBody = forms.CharField(widget=forms.Textarea(attrs={'label': '30'}),
                                   label='内容：', max_length=2000)

    # attrs={'label': "QuestionBody",},
    # label="QuestionBody",

    # page_length = forms.IntegerField(
    #     required=False, initial=25
    # )

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_id = 'id-exampleForm'
        # self.helper.form_method = 'get'
        # self.helper.form_action = 'adc'
        # self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            # Div(Field('page_length',
            #           template='pdemo/reports_condition.html',
            #           css_class='input-sm'
            #           ), css_class='box-header'),
            Div(css_class='box-header'),
            Fieldset(
                'Tell us your favorite stuff {{ username }}',
                'QuestionAuthor',
                'QuestionTitle',
                'QuestionSupply',
                'QuestionBody',
            ),
            FormActions(
                Submit('save_changes', 'Save changes', css_class="btn-primary"),
                # Submit('cancel', 'Cancel'),
                Reset('name', 'Cancel', css_class="btn-primary"),
            ),
        )


class Question(forms.ModelForm):
    class Meta:
        model = Bbs
        fields = '__all__'


class Answer(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'AnswerBody': Textarea(attrs={'class': 'vLargeTextField'}),
        }
        # labels = {
        #     'name': _('Writer'),
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }


class User(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        widget = forms.SelectMultiple(attrs={
            'class': 'form-control input-sm v-hidden',
            'data-toggle': 'query-select2',
            'multiple': 'multiple'
        })

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == '':
            raise forms.ValidationError("价格必须大于零")
        return name

# class ServerForm(forms.Form):
#     user = forms.CharField(label=_(u"名称"), max_length=30, required=True,
#                            widget=forms.TextInput(attrs={'size': 20,}))
#     ip = forms.IntegerField(label=_(u"IP地址"), max_length=20, required=True,
#                             widget=forms.TextInput(attrs={'size': 20,}))
#     port = forms.IntegerField(label=_(u"通信端口"), required=True,
#                               widget=forms.TextInput(attrs={'size': 20,}))
#     cpunum = forms.IntegerField(label=_(u"CPU个数"), required=True,
#                                 widget=forms.TextInput(attrs={'size': 20,}))
#     mem = forms.IntegerField(label=_(u"内存"), required=True,
#                              widget=forms.TextInput(attrs={'size': 20,}))
#     state = forms.CharField(label=_(u"状态"), max_length=30, required=True,
#                             widget=forms.TextInput(attrs={'size': 20,}))
