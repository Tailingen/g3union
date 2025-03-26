from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from mods.forms import ModCreateForm
from mods.models import Mod

class Home(ListView):
    model = Mod
    template_name = 'mods/home.html'
    context_object_name = 'posts'
    paginate_by = 10

def about(request):
    return render(request, 'mods/about.html')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Такой страницы не существует, глупый морра</h2>')

class ShowPost(DetailView):
    model = Mod
    template_name = 'mods/mod.html'
    context_object_name = 'post'

class CreatePost(CreateView):
    model = Mod
    form_class = ModCreateForm
    template_name = 'mods/create.html'
    #fields = ['slug', 'name', 'desc', 'content', 'is_published', 'category']
    success_url = reverse_lazy('home')

class UpdatePost(UpdateView):
    model = Mod
    template_name = 'mods/update.html'
    fields = ['name', 'desc', 'content', 'is_published', 'category']
    success_url = reverse_lazy('home')

class ShowCategory(ListView):
    model = Mod
    template_name = 'mods/category.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Mod.objects.filter()

