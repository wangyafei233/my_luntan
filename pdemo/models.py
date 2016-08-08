from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Field, Div
from django import forms
from django.utils.translation import ugettext as _
from django.db import models


class PublicModel(models.Model):
    start_time = models.DateField(help_text='输入有误')

    class Meta:
        abstract = True


class MessageForm(forms.Form):
    text_input = forms.CharField()
    textarea = forms.CharField(
        widget=forms.Textarea(),
    )
    radio_buttons = forms.ChoiceField(
        choices=(
            ('option_one',
             "Option one is this and that be sure to include why it's great"),
            ('option_two',
             "Option two can is something else and selecting it will deselect option one")
        ),
        widget=forms.RadioSelect,
        initial='option_two',
    )
    checkboxes = forms.MultipleChoiceField(
        choices=(
            ('option_one',
             "Option one is this and that be sure to include why it's great"),
            ('option_two',
             'Option two can also be checked and included in form results'),
            ('option_three',
             'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial='option_one',
        widget=forms.CheckboxSelectMultiple,
        help_text="<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )
    appended_text = forms.CharField(
        help_text="Here's more help text"
    )
    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()
    multicolon_select = forms.MultipleChoiceField(
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
    )
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
    helper.form_id = 'id-exampleForm'
    helper.form_action = 'shouye'
    helper.layout = Layout(
        Field('text_input', css_class='input-xlarge'),
        Field('textarea', rows="3", css_class='input-xlarge'),
        'radio_buttons',
        Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
        AppendedText('appended_text', '.00'),
        PrependedText('prepended_text',
                      '<input type="checkbox" checked="checked" value="" id="" name="">',
                      active=True),
        PrependedText('prepended_text_two', '@'),
        'multicolon_select',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )


class Report(PublicModel):
    name = models.CharField(_('Name'), max_length=255, unique=True, blank=True,)
    label = models.CharField(_('Label'), max_length=255, blank=True)
    order = models.IntegerField(default=0, )
