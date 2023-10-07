from django.shortcuts import render

from django.views.generic import ListView, DetailView

from blog.models import Blogpost


class BlogpostListView(ListView):
    model = Blogpost
    extra_context = {
        'title': f'Блог нашего сервиса',
    }


class BlogpostDetailView(DetailView):
    model = Blogpost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['object_list'] = Blogpost.objects.get(pk=self.kwargs.get('pk')),

        return context_data
