from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from clients.forms import ClientsForm
from clients.models import Client
from mailsender.models import Mailing


class ClientsCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientsForm
    template_name = 'clients/client_create.html'
    extra_context = {
        'title': f'Добавить нового получателя',
        'page_about': f'На этой странице вы можете добавить нового получателя ваших рассылок.'
    }

    def get_success_url(self):
        return reverse('clients:client_profile', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        self.object.user_id = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientsListView(ListView):
    model = Client


class ClientsDetailView(LoginRequiredMixin, DetailView):
    model = Client

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(pk=self.kwargs.get('pk'))
    #     return queryset


class ClientsUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientsForm
    template_name = 'clients/client_create.html'

    def get_success_url(self):
        return reverse('clients:client_profile', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        self.object.user_id = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients:clients_list')
