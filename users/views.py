from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from requests import request

from .forms import CustomUserCreationForm

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['auth_user'] = get_user(self.request)
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'user_update.html'
    context_name = 'user'
    login_url = 'login'
    fields = ['first_name', 'last_name', 'email', 'age']

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def get_success_url(self) -> str:
        return reverse_lazy('user_detail', kwargs={'pk':self.request.user.pk})