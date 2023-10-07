from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientsListView, ClientsCreateView, ClientsDetailView, ClientsUpdateView, ClientDeleteView

app_name = ClientsConfig.name


urlpatterns = [
    path('', ClientsListView.as_view(), name='clients_list'),
    path('add/', ClientsCreateView.as_view(), name='add_client'),
    path('profile/<int:pk>', ClientsDetailView.as_view(), name='client_profile'),
    path('update/<int:pk>', ClientsUpdateView.as_view(), name='client_update'),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    ]
