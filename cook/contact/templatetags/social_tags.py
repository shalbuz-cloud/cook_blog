from django import template
from ..models import Social, About

register = template.Library()


@register.simple_tag()
def get_social_links():
    """Вывод ссылок социальных сетей"""
    return Social.objects.all()


@register.simple_tag()
def get_about():
    """Вывод about"""
    return About.objects.last()
