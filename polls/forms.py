from django import forms
from .models import Question, Choice
from django.contrib.admin import widgets
from django.forms.models import modelform_factory
from datetimewidget.widgets import DateTimeWidget
from django.forms import ModelForm


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class TestForm(forms.Form):
    QuestionForm = modelform_factory(Question, fields=['question_text'])({})
    ChoiceForm = modelform_factory(Choice, fields=['choice_text'])({})
    question = forms.CharField(label="Question text", max_length=QuestionForm.fields['question_text'].max_length)
    choice = forms.CharField(label="Choice text", max_length=ChoiceForm.fields['choice_text'].max_length)
    pub_date = forms.DateTimeField(label='Date and time', widget=widgets.AdminSplitDateTime())
    # pub_date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    # pub_date = forms.SplitDateTimeField(label='Date and time')


class QuestionForm(ModelForm):
    class Meta:
        model = Question

    # def __init__(self, *args, **kwargs):

        fields = ('question_text', 'pub_date', )


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text', )
