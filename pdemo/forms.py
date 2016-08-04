#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from crispy_forms.bootstrap import FormActions, AppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Field, Div, \
    ButtonHolder, HTML, Reset, Button
from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from mydemo.pdemo.models import Report


class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label="Do you like this website?",
        choices=((1, "Yes"), (0, "No")),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect,
        initial='1',
        required=True,
    )

    favorite_food = forms.CharField(
        label="What is your favorite food?",
        max_length=80,
        required=True,
    )

    favorite_color = forms.CharField(
        label="What is your favorite color?",
        max_length=80,
        required=True,
    )

    favorite_number = forms.IntegerField(
        label="Favorite number",
        required=False,
    )

    notes = forms.CharField(
        label="Additional notes or feedback",
        required=False,
    )
    page_length = forms.IntegerField(
        required=False, initial=25
    )

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_method = 'get'
        self.helper.form_action = 'adc'
        # self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Div(Field('page_length',
                      template='pdemo/reports_condition.html',
                      css_class='input-sm'
                      ), css_class='box-header'),
            Fieldset(
                'Tell us your favorite stuff {{ username }}',
                'like_website',
                'favorite_number',
                'favorite_color',
                'favorite_food',
                HTML("""
            <p>We use notes to get better, <strong>please help us {{ username }}</strong></p>
        """),
                'notes',
            ),
            FormActions(
                Submit('save_changes', 'Save changes', css_class="btn-primary"),
                Submit('cancel', 'Cancel'),
            ),

        )


class ServerForm(forms.Form):
    user = forms.CharField(label=_(u"名称"), max_length=30, required=True,
                           widget=forms.TextInput(attrs={'size': 20,}))
    ip = forms.IPAddressField(label=_(u"IP地址"), max_length=20, required=True,
                              widget=forms.TextInput(attrs={'size': 20,}))
    port = forms.IntegerField(label=_(u"通信端口"), required=True,
                              widget=forms.TextInput(attrs={'size': 20,}))
    cpunum = forms.IntegerField(label=_(u"CPU个数"), required=True,
                                widget=forms.TextInput(attrs={'size': 20,}))
    mem = forms.IntegerField(label=_(u"内存"), required=True,
                             widget=forms.TextInput(attrs={'size': 20,}))
    state = forms.CharField(label=_(u"状态"), max_length=30, required=True,
                            widget=forms.TextInput(attrs={'size': 20,}))


class User(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('name', 'label', 'order')
        widget = {
            'name': {},
        }
