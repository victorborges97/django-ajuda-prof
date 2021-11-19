from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse

class Categoria(models.Model):
    titulo = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.titulo

class Post(models.Model):
    post_title = models.CharField(max_length=250, null=True)
    post_content = RichTextField(blank=True, null=True)
    post_create = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="blog_posts_likes")

    def __str__(self):
        return self.post_title

    def total_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self): # new
        return reverse('posts:post_detail', kwargs={'pk': self.id},)

class Comment(models.Model):
    comment_text = models.TextField()
    comment_create = models.DateTimeField(auto_now_add=True)
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.comment_text