from django import template

register = template.Library()

@register.filter
def cap_all_but_upper_first(value):
    if value.lower() == "admin":
        return value.upper()
    else: 
        return value.capitalize()