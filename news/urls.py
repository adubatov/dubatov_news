from django.urls import path
from .views import (
    HomePageView, 
    NewsListView, 
    NewsDetailView, 
    NewsUpdateView, 
    NewsDeleteView, 
    NewsCreateView
)

urlpatterns = [
    # path('articles/<int:pk>', HomePageView.as_view(), name='home')
    path('', HomePageView.as_view(), name='home'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),

]
