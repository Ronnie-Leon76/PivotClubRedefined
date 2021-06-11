from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Article


# Create your views here.

class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article


class ArticleUpdateView(UpdateView):
    model = Article


class ArticleDeleteView(DeleteView):
    model = Article
