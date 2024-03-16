from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'blog/index.html'


class BlogPageView(TemplateView):
    template_name = 'blog/blog.html'

class AboutPageView(TemplateView):
    template_name = 'blog/about.html'

class InfoPageView(TemplateView):
    template_name = 'blog/info.html'
