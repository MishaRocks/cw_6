from django.http import Http404
from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from mailsender.forms import MailingForm, MessageFormSet
from mailsender.models import Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailsender:mail-list')

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Создаем экземпляр формсета для сообщений
        message_formset = MessageFormSet(self.request.POST)

        if message_formset.is_valid():
            # Если формсет сообщений валиден, сохраняем сообщения
            messages = message_formset.save(commit=False)
            for message in messages:
                message.save()

            # Привязываем сообщения к рассылке
            form.instance.message.set(messages)
        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing

    def get_queryset(self):
        if self.request.user.is_staff:
            return Mailing.objects.all()
        queryset = Mailing.objects.filter(user=self.request.user, is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailsender_count'] = self.object_list.count()
        context['active_mails_count'] = self.object_list.filter(status='started').count()


class MailingDetailView(DetailView):
    model = Mailing

    def get_object(self, queryset=None):
        return get_object_or_404(Mailing, pk=self.kwargs['pk'])


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailsender:mail-list')
    permission_required = 'mailing.change_mailingsettings'

    def has_permission(self):
        obj = self.get_object()
        if self.request.user == obj.user or self.request.user.is_staff:
            return True
        return super().has_permission()


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailsender:mail-list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404()
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            self.object.delete()
            return self.success_url
        else:
            raise Http404()
