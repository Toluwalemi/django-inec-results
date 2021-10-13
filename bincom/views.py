from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Agentname


class BlogListView(ListView):
    model = Agentname
    template_name = 'home.html'
