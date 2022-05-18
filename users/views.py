from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

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