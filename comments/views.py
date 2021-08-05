from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import CommentCreationForm
from .models import Comment

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'comment/create.html'

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'pk':self.object.article.pk})