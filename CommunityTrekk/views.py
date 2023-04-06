from django.shortcuts import render
from django.views.generic import ListView, DetailView
from CommunityTrekk.models import Post



def index(request):
    return render(request, "CommunityTrekk/index.html")


class PostList(ListView):
    model= Post
    
    
class PostDetail(DetailView):
    model= Post
    
    

