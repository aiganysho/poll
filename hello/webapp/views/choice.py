from django.shortcuts import reverse, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Poll, Choice
from webapp.form import ChoiceForm
from django.urls import reverse_lazy


class ChoiceView(ListView):
    template_name = 'choice/choice.html'
    model = Choice
    context_object_name = 'answers'


class ChoiceDetailView(DetailView):
    model = Choice
    template_name = 'choice/choice_view.html'


class ChoiceCreate(CreateView):
    template_name = 'choice/choice_create.html'
    form_class = ChoiceForm
    model = Choice
    #
    # def form_valid(self, form):
    #     poll = get_object_or_404(Poll, id=self.kwargs.get('pk'))
    #     answer = form.save(commit=False)
    #     answer.poll = poll
    #     answer.save()
    #     form.save_m2m()
    #     return redirect(reverse('view-poll', kwargs={'pk': poll.pk}))

    def get_success_url(self):
        return reverse(
            'view-poll',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        poll = get_object_or_404(Poll, id=self.kwargs.get('pk'))
        form.instance.poll = poll
        return super().form_valid(form)


class ChoiceUpdate(UpdateView):
    model = Choice
    template_name = 'choice/choice_update.html'
    form_class = ChoiceForm
    context_object_name = 'answer'

    def get_success_url(self):
        return reverse('view-choice', kwargs={'pk': self.kwargs.get('pk')})

class ChoiceDelete(DeleteView):
    model = Choice
    template_name = 'choice/choice_delete.html'
    context_object_name = 'answer'
    success_url = reverse_lazy('list-choice')

