from django import template
register = template.Library()
import datetime
from ..models import Category



@register.simple_tag(name='days')
def current_time(format_string):
    d0 = datetime.datetime.now().date()
    d1 = format_string.created.date()
    delta = d0 - d1
    return delta.days

@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    timezone = context['timezone']
    return your_get_current_time_method(timezone, format_string)


@register.inclusion_tag('categories/category_list.html')
def category_list_tag(category_objs):
    return {'category_objs':category_objs }

# @register.assignment_tag(name='')
# def any_function(count=5):
#     return *some database query*