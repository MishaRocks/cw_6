from django.urls import path

from mailsender.apps import MailsenderConfig
from mailsender.views import MailingListView, MailingCreateView, MailingDetailView, MailingUpdateView

app_name = MailsenderConfig.name

urlpatterns = [
    path('new/', MailingCreateView.as_view(), name='mail-create'),
    path('', MailingListView.as_view(), name='mail-list'),
    path('<int:pk>/', MailingDetailView.as_view(), name='mail-detail'),
    path('<int:pk>/edit/', MailingUpdateView.as_view(), name='mail-edit'),
]
