from typing import Collection
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ContentCollection, Content
from .forms import ContentForm

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def collections_index(request):
  content_collection = ContentCollection.objects.filter(user=request.user)
  return render(request, 'collections/index.html', {'collections':content_collection})

def collections_detail(request, collection_id):
  collection = ContentCollection.objects.get(id=collection_id)
  content_form = ContentForm()
  return render(request, 'collections/detail.html', { 'collection': collection, 'content_form': content_form })

def add_content(request, collection_id):
  form = ContentForm(request.POST)
  if form.is_valid():
    new_content= form.save(commit=False)
    new_content.collection_id = collection_id
    new_content.save()
  return redirect('collections_detail', collection_id=collection_id)

def delete_content(request, collection_id, content_id):
  content = Content.objects.get(id=content_id)
  content.delete()
  return redirect('collections_detail', collection_id=collection_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('collections_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class CollectionCreate(CreateView):
  model = ContentCollection
  fields = ['name', 'description']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class CollectionDelete(DeleteView):
  model = ContentCollection
  success_url = '/collections/'