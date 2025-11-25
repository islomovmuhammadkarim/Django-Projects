from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

class ArticleList(LoginRequiredMixin,ListView):
    model=Article
    template_name="articles/article_list.html"
    context_object_name="articles"
    ordering=['title']


class ArticleDetail(LoginRequiredMixin,DetailView):
    model=Article
    template_name="articles/article_detail.html"
    context_object_name="article"

class ArticleUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Article
    template_name="articles/article_update.html"
    fields=['title','summary','body','photo']
    success_url=reverse_lazy('article-list')

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user

class ArticleDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Article
    template_name="articles/article_delete.html"
    success_url=reverse_lazy('article-list')

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user


class ArticleCreate(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Article
    template_name="articles/article_create.html"
    fields=['title','summary','body','photo']
    success_url=reverse_lazy('article-list')    

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser