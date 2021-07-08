from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from blog.forms import AddArticle
from blog.models import Article


# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'article'
    paginate_by = 4


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    # adds additional data
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)


class ArticleCreateView(CreateView):
    """
    - takes model to be utilised
    - form_class if any
    - template_name
    - success_url
    """
    model = Article
    form_class = AddArticle
    template_name = 'blog/article_create.html'
    success_url = 'blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        messages.success(self.request,
                         ' Thank you, your review has been successfully submitted and is awaiting moderation.')
        return super(ArticleCreateView, self).form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'blog/article_create.html'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog/article_delete.html'


class ArticleGenreView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'article'
    paginate_by = 2

    def get_queryset(self):
        return Article.objects.filter(genre__icontains=self.kwargs.get('genre'))
