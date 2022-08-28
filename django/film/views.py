from django.shortcuts import render
from django.views import generic
from .models import *

class IndexView(generic.ListView):
    template_name = 'index.html'
    model = Director

class DirectorDetail(generic.DetailView):
    template_name = 'director.html'
    model = Director

class FilmDetail(generic.DetailView):
    template_name = 'film.html'
    model = Film


