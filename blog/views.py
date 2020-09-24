from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class BlogView(TemplateView):
    template_name = 'blog/all_blog.html'
