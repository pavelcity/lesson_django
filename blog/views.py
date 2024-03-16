from django.contrib.auth import logout
from django.shortcuts import render, redirect
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


def logout_user(request):
    logout(request)
    return redirect('home')
