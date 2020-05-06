from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Bookmark
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list') # 글쓰기를 완료했을 때 이동할 페이지
    template_name_suffix = '_create'


class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6
