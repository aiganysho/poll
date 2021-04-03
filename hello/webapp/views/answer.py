from django.shortcuts import reverse, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from webapp.models import Poll, Choice, Answer
from webapp.form import AnswerForm
from django.urls import reverse_lazy


class AnswerView(ListView):
    template_name = 'choice/choice.html'
    model = Answer