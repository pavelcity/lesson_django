from itertools import chain

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView

from .models import *

# Create your views here.
class HomePageView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        blog = Blog.objects.filter(is_published=True)[:4]
        all_content = list(chain(blog))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = [content for content in context['all_content'] if isinstance(content, Blog)]
        return context



class BlogPageView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'all_content'

    def get_queryset(self):
        blog = Blog.objects.filter(is_published=True).order_by('-time_create')
        all_content = list(chain(blog))
        return all_content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = [content for content in context['all_content'] if isinstance(content, Blog)]
        return context


class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog/blogdetail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'blog'


class AboutPageView(TemplateView):
    template_name = 'blog/about.html'



class InfoPageView(TemplateView):
    template_name = 'blog/info.html'


def logout_user(request):
    logout(request)
    return redirect('home')
