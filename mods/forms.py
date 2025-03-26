from django import forms

from mods.models import Mod


class ModCreateForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'slug', 'desc', 'content', 'is_published', 'category']
        model = Mod
        widgets = {'desc': forms.Textarea(attrs={'cols': 50, 'rows': 10}), 'content': forms.Textarea(attrs={'cols': 100, 'rows': 20})}
        labels = {'name': 'Название', 'desc': 'Сведения', 'content': 'Текст', 'is_published': 'Опубликовать', 'category': 'Категория'}
