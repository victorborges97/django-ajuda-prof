from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Post, Categoria, Comment
from .forms import CommentForm, PostForm, PostFormEdit
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

import logging

logger = logging.getLogger(__name__)

class HomePageView(TemplateView):
    template_name = "home.html"

class BlogPageView(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super(BlogPageView, self).get_context_data(**kwargs)
        latest_post_list = Post.objects.order_by("-post_create")[:5]
        context['posts'] = latest_post_list
        context['categorias'] = Categoria.objects.all()
        return context

class BlogDatailPostPageView(TemplateView):
    template_name = "blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BlogPageView, self).get_context_data(**kwargs)
        post = Post.objects.get(pk=post_id)
        logging.debug(post)
        context['post'] = post
        return context

class postDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"

class updatePostView(UpdateView):
    model = Post
    form_class = PostFormEdit
    template_name = "blog_update_post.html"

class addPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog_add_post.html"

def likeView(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('posts:blog'))

def add_comment(request, post_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.comment_post_id = post_id
            data.comment_author = request.user
            data.save()
        return HttpResponseRedirect(url+"#comentarios")
    return HttpResponseRedirect(url+"#comentarios")

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    logging.debug(post)
    return render(request, "blog_detail.html", { 
        'post': post,
    })

def results(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = { 
        'post': post,
    }
    return HttpResponse("Essa é o resultado do post de número %s"% post_id)

def ver_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    return render(request, "ver_categoria.html", {
        'categoria': categoria,
        'posts': Post.objects.filter(post_categoria=categoria)[:5]
    })