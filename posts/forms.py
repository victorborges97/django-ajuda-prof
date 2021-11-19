from django import forms
from django.contrib.auth.models import Group

from .models import Comment, Post

class LocalSignupForm(forms.Form):
    pass

    def signup(self, request, user):
        g = Group.objects.get(pk=1)
        user.groups.add(g)
        user.is_staff = False
        user.save()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title', 'post_author', 'post_content', 'post_categoria',)

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Titulo da postagem"}),
            'post_author': forms.TextInput(attrs={'class': 'form-control', 'id': 'elder', 'value':'', 'type': 'hidden'}),
            'post_content': forms.Textarea(attrs={'class': 'form-control'}),
            'post_categoria': forms.Select(attrs={'class': 'form-control'})
        }

class PostFormEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("post_title", "post_content", "post_categoria",)

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Titulo da postagem"}),
            'post_content': forms.Textarea(attrs={'class': 'form-control'}),
            'post_categoria': forms.Select(attrs={'class': 'form-control'})
        }