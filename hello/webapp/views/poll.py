from django.shortcuts import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Poll, Choice
from webapp.form import PollForm, ChoiceForm
from django.urls import reverse_lazy

class IndexView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    context_object_name = 'lists'
    paginate_by = 5
    paginate_orphans = 1



class PollDetailView(DetailView):
    template_name = 'poll/poll_detail.html'
    context_key = 'poll'
    model = Poll


class PollCreate(CreateView):
    template_name = 'poll/poll_create.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse(
            'view-poll',
            kwargs={'pk': self.object.pk}
        )


class PollUpdate(UpdateView):
    model = Poll
    template_name = 'poll/poll_update.html'
    form_class = PollForm
    context_key = 'poll'
    def get_success_url(self):
        return reverse(
            'view-poll',
            kwargs={'pk': self.object.pk}
        )



class PollDelete(DeleteView):
    template_name = 'poll/poll_delete.html'
    model = Poll
    context_key = 'poll'
    success_url = reverse_lazy('list-poll')

