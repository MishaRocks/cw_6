from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogpostListView, BlogpostDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogpostListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogpostDetailView.as_view(), name='post'),
    ]
