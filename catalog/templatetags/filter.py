from django import template

register = template.Library()


@register.filter
def slice(text, len_=100):
    return text[:len_] + ' ...'
