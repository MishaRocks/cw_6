from django.urls import path

from mailsender.apps import MailsenderConfig
from mailsender.views import ClientCreateView, MailingListView

app_name = MailsenderConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='index'),
    path('client/new/', ClientCreateView.as_view(), name='new_client'),
]