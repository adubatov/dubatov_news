from django import forms

from .models import Comment

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # comment = forms.CharField(widget=forms.Textarea())
        fields = ['comment']
        auto_id = False