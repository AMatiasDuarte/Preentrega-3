from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from CommunityTrekk.models import Post, Profile, Mensaje
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about_mi(request):
    return render(request, "CommunityTrekk/about_mi.html")



def index(request):
    context= {
            "posts": Post.objects.all()
        
    }
    return render(request, "CommunityTrekk/index.html", context)


class PostList(ListView):
    model= Post
    
    
class PostDetail(DetailView):
    model= Post
    
    
class PostCreate(LoginRequiredMixin, CreateView):
    model= Post
    success_url= reverse_lazy("post-list")
    fields= '__all__'
    
class PostUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model= Post
    success_url= reverse_lazy("post-list")
    fields= '__all__'

    def test_func(self):
        user_id= self.request.user.id
        post_id= self.kwargs.get('pk')
        return Post.objects.filter(publisher= user_id, id= post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "CommunityTrekk/not_found.html")
    
class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Post
    success_url= reverse_lazy("post-list")

    def test_func(self):
        user_id= self.request.user.id
        post_id= self.kwargs.get('pk')
        return Post.objects.filter(publisher= user_id, id= post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "CommunityTrekk/not_found.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name= 'registration/signup.html'
    success_url= reverse_lazy('post-list')
    
class Login(LoginView):
    next_page= reverse_lazy('post-list')

class Logout(LogoutView):
    template_name= 'registration/logout.html'    


class ProfileUpdate(UpdateView):
    model= Profile
    fields= '__all__'
    
class ProfileCreate(LoginRequiredMixin, CreateView):
    model= Profile
    fields= '__all__'
    success_url= reverse_lazy("post-list")
   
class ProfileList(LoginRequiredMixin, ListView):
    model= Profile
    context_object_name= "profiles" 

    
class MensajeCreate(CreateView):
    model= Mensaje
    fields= '__all__'
    success_url= reverse_lazy("post-list")
    
    
class MensajeList(LoginRequiredMixin, ListView):
    model= Mensaje
    context_object_name= "mensajes"
    
    def get_queryset(self):
        return Mensaje.objects.filter(destinatario= self.request.user.id).all()
    
    
class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Mensaje
    success_url= reverse_lazy("mensaje-list")
    
    def test_func(self):
        user_id= self.request.user.id
        mensaje= self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario= user_id).exists()