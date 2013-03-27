from django import template
from ui_patterns.models import Pattern

register = template.Library()

@register.inclusion_tag('ui_patterns/tag_pattern_list.html')
def pattern_list():
    patterns = Pattern.objects.live()
    return { 'patterns': patterns }
