import django_filters
from django.forms import CheckboxSelectMultiple, SelectMultiple, NumberInput
from django.shortcuts import render

from .models import Glider, Maker, Size, CERTIFICATION_CHOICES
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



class SizeFilter(django_filters.FilterSet):
    certification = ChoiceFilter(field_name= "certification", choices=CERTIFICATION_CHOICES)
    cells = RangeFilter(field_name="cells", lookup_expr='icontains')
    gliderWeight = RangeFilter(field_name="gliderWeight", lookup_expr='icontains')
    projectArea = RangeFilter(field_name="projectAreat", lookup_expr='icontains')
    flatArea = RangeFilter(field_name="flatArea", lookup_expr='icontains')

