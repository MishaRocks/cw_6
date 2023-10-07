from django.views.generic import ListView

from logs.models import Logs


class MailingLogListView(ListView):
    model = Logs
    context_object_name = 'mailing_logs'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Logs.objects.all()
        queryset = Logs.objects.filter(mailing__user=self.request.user)
        return queryset
