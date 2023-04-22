from django.views.generic import *
from django.shortcuts import render
from SecondMarket.models import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import *
from django.contrib.auth.views import *
from django.contrib.auth.mixins import *



def about(request):
    return render(request, "SecondMarket/about.html")


def index(request):
    
    context = {
        "posts":  Post.objects.all()
    }
    return render(request, "SecondMarket/index.html", context)


class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'
    
    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(DueñoPost=user_id, id=post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "SecondMarket/not_found.html")




class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(DueñoPost=user_id, id=post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "SecondMarket/not_found.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')

class Login(LoginView):
    next_page = reverse_lazy("index")

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class ProfileUpdate(UpdateView):
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('index')

class ProfileCreate(CreateView):
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('index')

class MensajeCreate(CreateView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy('index')

class MensajeList(LoginRequiredMixin,ListView):
    model = Mensaje
    
    def get_queryset(self):
        return Mensaje.objects.filter(destinatario = self.request.user.id).all()

class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-list')
    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario=user_id).exists()
