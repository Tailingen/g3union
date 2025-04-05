from django.http import HttpResponse
from django.urls import path, register_converter
from mods.converter import CustomConverter
from mods import views

register_converter(CustomConverter, 'years')

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('mods/<slug:post_slug>', views.ShowPost.as_view(), name='show_post'),
    path('mods/create/', views.CreatePost.as_view(), name='create'),
    path('mods/update/<int:pk>', views.UpdatePost.as_view(), name='update'),
    path('mods/delete/<int:pk>', views.DeletePost.as_view(), name='delete'),
    path('mods/cat/<slug:slug>', views.ShowCategory.as_view(), name='category'),
    path('mods/tag/<slug:slug>', views.ShowTag.as_view(), name='tag'),
]