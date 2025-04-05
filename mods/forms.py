from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

from mods.models import Mod, Category


class ModCreateForm(forms.ModelForm):
    slug = forms.SlugField(max_length=100, label='URL',
                           validators=[
                               MinLengthValidator(2, message='Минимум 2 символа'),
                               MaxLengthValidator(100, message='Максимум 100 символов')
                           ])
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категория')

    class Meta:
        fields = ['name', 'slug', 'desc', 'content', 'is_published', 'category']
        model = Mod
        widgets = {'desc': forms.Textarea(attrs={'cols': 50, 'rows': 10}), 'content': forms.Textarea(attrs={'cols': 100, 'rows': 20})}
        labels = {'name': 'Название', 'desc': 'Сведения', 'content': 'Текст', 'is_published': 'Опубликовать', 'category': 'Категория'}
