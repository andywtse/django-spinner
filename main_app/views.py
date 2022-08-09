from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ContentCollection

def home(request):
  return render(request, 'home.html')

def collections_index(request):
  content_collection = ContentCollection.objects.all()
  return render(request, 'collections/index.html', {'collections':content_collection})