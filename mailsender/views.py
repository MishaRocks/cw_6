from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from mailsender.models import Client, Mailing


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailsender/index.html'
    extra_context = {
        'title': 'Рассылки',
        'page_about': 'Рассылки, представленные на сайте.'
    }


class ClientCreateView(CreateView):
    model = Client
    template_name = 'mailsender/client_create.html'
    fields = ('email', 'name', 'surname', 'comment')
    success_url = reverse_lazy('mailsender:index')
    extra_context = {
        'title': 'Регистрация нового пользователя',
        'page_about': 'После регистрации вы сможете создать свои рассылки'
    }
