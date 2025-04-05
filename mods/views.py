from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from mods.forms import ModCreateForm
from mods.models import Mod

class Home(ListView):
    #model = Mod
    template_name = 'mods/home.html'
    context_object_name = 'posts'
    paginate_by = 10
    extra_context = {'title': 'Список модов'}

    def get_queryset(self):
        return Mod.published.all()

def about(request):
    return render(request, 'mods/about.html', {'title': 'О сайте'})

def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Такой страницы не существует, глупый морра</h2>')

class ShowPost(DetailView):
    #model = Mod
    template_name = 'mods/mod.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    #extra_context = {'title': 'X'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_object_or_404(Mod.published, slug=self.kwargs[self.slug_url_kwarg]).name
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Mod.published, slug=self.kwargs[self.slug_url_kwarg])



class CreatePost(CreateView):
    model = Mod
    form_class = ModCreateForm
    template_name = 'mods/create.html'
    #fields = ['slug', 'name', 'desc', 'content', 'is_published', 'category']
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Создать пост'}

class UpdatePost(UpdateView):
    model = Mod
    template_name = 'mods/update.html'
    fields = ['name', 'desc', 'content', 'is_published', 'category']
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Редактировать пост'}

class DeletePost(DeleteView):
    model = Mod
    template_name = 'mods/delete.html'
    success_url = reverse_lazy('home')

class ShowCategory(ListView):
    #model = Mod
    template_name = 'mods/category.html'
    context_object_name = 'posts'
    paginate_by = 10
    extra_context = {'title': 'статьи по категориям'}

    def get_queryset(self):
        return Mod.published.filter(category__slug=self.kwargs['slug'])


class ShowTag(ListView):
    #model = Mod
    template_name = 'mods/tag.html'
    context_object_name = 'posts'
    paginate_by = 10
    extra_context = {'title': 'статьи по тэгу'}

    def get_queryset(self):
        return Mod.published.filter(tags__slug=self.kwargs['slug'])


