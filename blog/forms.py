from django import forms
from .models import Article


class AddArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body', 'photo', 'genre')
