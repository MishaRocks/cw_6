from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from mailsender.models import Mailing


class MailingListView(ListView):
    ...
