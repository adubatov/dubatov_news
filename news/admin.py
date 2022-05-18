from datetime import datetime

from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'article', 'author', 'format_date')

    @admin.display(description='Date')
    def format_date(self, obj):
        return datetime.strftime(obj.pub_date, '%d.%m.%Y, %H:%M:%S')


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)