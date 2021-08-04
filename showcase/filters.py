import django_filters
from django.forms import CheckboxSelectMultiple, SelectMultiple, NumberInput

from .models import Glider, Maker, Size
from django_filters import CharFilter, NumberFilter, NumericRangeFilter, ChoiceFilter, RangeFilter



class GliderFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr='icontains')
    maker = django_filters.ModelMultipleChoiceFilter(
        queryset=Maker.objects.all(),
        field_name="maker__name",
        widget=SelectMultiple(),
        label="manufactures",
        label_suffix="",
    )
    year = RangeFilter(field_name="year", lookup_expr='icontains')

