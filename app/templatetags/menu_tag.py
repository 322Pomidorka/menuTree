from django import template
from django.core.paginator import Paginator
from django.db.models import Prefetch

from ..models import Menu

register = template.Library()


@register.inclusion_tag(filename="templatetags/menu.html", takes_context=True)
def draw_menu(context, slug_menu):
    data = {}

    data['menu_list'] = Menu.objects.filter(slug=slug_menu).prefetch_related('children')
    if not len(data['menu_list']):
        data['error'] = f"Menu by {slug_menu} keyword not found"

    return {'menu': data, "request": context["request"]}
