from django import template
import mods.models as models

register = template.Library()

@register.inclusion_tag('mods/list_categoryes.html')
def show_categoryes():
    cats = models.cats_list
    return {'cats': cats}