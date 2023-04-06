from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from CommunityTrekk.models import Post
from django.urls import reverse_lazy



def index(request):
    return render(request, "CommunityTrekk/index.html")


class PostList(ListView):
    model= Post
    
    
class PostDetail(DetailView):
    model= Post
    
    
class PostCreate(CreateView):
    model= Post
    success_url= reverse_lazy("post-list")
    fields= '__all__'
    
class PostUpdate(UpdateView):
    model= Post
    success_url= reverse_lazy("post-list")
    fields= '__all__'
    

