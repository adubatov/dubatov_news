from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, 
    ListView, 
    UpdateView, 
    DetailView, 
    DeleteView, 
    CreateView,)
from django.views.generic.edit import FormMixin
from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Article, Comment
from .forms import CreateCommentForm

from pprint import pprint

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'articles'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()
        return context


class NewsListView(FormMixin, ListView):
    model = Article
    template_name = 'news_list.html'
    context_object_name = 'articles'
    form_class = CreateCommentForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(self.get_queryset()[0].pk)
        # pk = self.kwargs['pk']
        form = CreateCommentForm()
        # article = get_object_or_404(Article, pk=pk)

        context['latest_articles'] = Article.objects.all()
        context['form'] = form
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        
        form = CreateCommentForm(request.POST)
        return self.get(request, *args, **kwargs)


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


class NewsDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Article
    template_name = "news_detail.html"
    login_url = 'login' 
    form_class = CreateCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(self.get_queryset()[0].pk)
        # pk = self.kwargs['pk']
        form = CreateCommentForm()
        # article = get_object_or_404(Article, pk=pk)
        context['form'] = form
        return context

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = CreateCommentForm(self.request.POST)
        print('='*30)
        print(form.as_p())
        print('='*30)

        if form.is_valid():
            form.instance.article = self.object
            form.instance.author = get_user(self.request)
            form.save()
            return HttpResponseRedirect(self.object.get_absolute_url())
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)



class NewsCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'news_create.html'
    fields = ['title', 'body']
    login_url = 'login'   


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

