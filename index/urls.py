from django.urls import path

from index.apps import IndexConfig
from index.views import indexview

app_name = IndexConfig.name
urlpatterns = [
    path('', indexview, name='index_page'),
    ]