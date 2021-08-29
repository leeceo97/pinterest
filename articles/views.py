from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articles.decorator import article_ownership_required
from articles.forms import ArticleCreationForm
from articles.models import Article
from comments.forms import CommentCreationForm



class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articles/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'pk': self.object.pk})

class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articles/detail.html'


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articles/update.html'

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articles/delete.html'
    success_url = reverse_lazy('articles:list')

class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articles/list.html'
    paginate_by = 2