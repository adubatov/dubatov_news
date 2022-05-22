from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse



class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"pk": self.pk})

    

class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name = 'comments')
    comment = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("news_list", kwargs={"pk": self.pk})
    