from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articles.models import Article
from .decorator import comment_ownership_required
from .forms import CommentCreationForm
from .models import Comment

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'comment/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'pk':self.object.article.pk})

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/delete.html'
    context_object_name = 'target_comment'

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'pk':self.object.article.pk})