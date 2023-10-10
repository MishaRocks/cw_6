from django.urls import path

from logs.apps import LogsConfig
from logs.views import MailingLogListView

app_name = LogsConfig.name

urlpatterns = [
    path('', MailingLogListView.as_view(), name='logs-list'),
]
