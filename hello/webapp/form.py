from django import forms
from django.forms import ModelForm
from webapp.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('question',)


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('text',)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('poll', 'choice_answer')