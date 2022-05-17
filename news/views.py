from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, 
    ListView, 
    UpdateView, 
    DetailView, 
    DeleteView, 
    CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Article

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'articles'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()
        return context


class NewsListView(ListView):
    model = Article
    template_name = 'news_list.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()
        return context


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "news_update.html"
    fields = ['title', 'body']
    sucess_url = reverse_lazy('news_list')
    login_url = 'login'   

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "news_delete.html"
    success_url = reverse_lazy('news_list')
    login_url = 'login'   

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author


class NewsDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "news_detail.html"
    login_url = 'login'   



class NewsCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'news_create.html'
    fields = ['title', 'body']
    login_url = 'login'   


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
