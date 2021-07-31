import django_filters
from .models import Glider
from django_filters import CharFilter

class GliderFilter(django_filters.FilterSet):
    title = CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Glider
        fields = ['name']