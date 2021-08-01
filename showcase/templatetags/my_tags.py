from django import template

# questo tag serve per evitare duplicati causa filtri django nel file cards.html causa infintie scroll pagination

register = template.Library()


@register.simple_tag(takes_context=True)
def relative_url(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    return query.urlencode()
