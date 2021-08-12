import django_filters
from django.db import models
from django.forms import ModelForm, CheckboxSelectMultiple, SelectMultiple, NumberInput, TextInput
from django.shortcuts import render
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, ButtonHolder, Submit, Row, Column
from crispy_forms.bootstrap import StrictButton

from django import forms
from .models import Glider, Maker, Size, CERTIFICATION_CHOICES
from django_filters import CharFilter,  NumberFilter, NumericRangeFilter, ChoiceFilter, RangeFilter, MultipleChoiceFilter
from django_filters.fields import RangeField

from .widgets import CustomRangeWidget


class GliderFilterForm(ModelForm):

    class Meta:
        model = Glider
        fields = [
            'name',
            'maker',
            'year',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-sm-3 mb-0'),


                Column('maker', css_class='form-group col-sm-5 mb-0'),


                Column('year', css_class='form-group col-6 mb-0'),

                css_class='form-row'
            ),
        )

class YearFilterFormHelper(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'get'
        layout_fields = []
        for field_name, field in self.fields.items():
            if isinstance(field, RangeField):
                layout_field = Field(field_name, template="showcase/fields/range-slider.html")
            else:
                layout_field = Field(field_name)
            layout_fields.append(layout_field)
        layout_fields.append(StrictButton("Submit", name='submit', type='submit', css_class='btn btn-fill-out btn-block mt-1'))
        self.helper.layout = Layout(*layout_fields)

class YearRangeFilter(RangeFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        values = [g.year for g in Glider.objects.all()]
        min_value = min(values)
        max_value = max(values)
        self.extra['widget'] = CustomRangeWidget(attrs={'data-range_min':min_value,'data-range_max':max_value})


class GliderFilter(django_filters.FilterSet):

    name = CharFilter(field_name="name", label="",lookup_expr='icontains', widget=TextInput(attrs={
        'placeholder': 'Search by Name...'
    }))


    maker = django_filters.ModelChoiceFilter(
        label='',
        empty_label=('Manufacturer'),
        field_name="maker__name",

        label_suffix="",
    )
    year = YearRangeFilter()

    class Meta:
        form = GliderFilterForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['maker'].queryset = Maker.objects.all()





class SizeFilter(django_filters.FilterSet):
    certification = MultipleChoiceFilter(field_name= "certification", choices=CERTIFICATION_CHOICES, widget=CheckboxSelectMultiple)
    cells = RangeFilter(field_name="cells", lookup_expr='icontains')
    gliderWeight = RangeFilter(field_name="gliderWeight", lookup_expr='icontains')
    projectArea = RangeFilter(field_name="projectArea", lookup_expr='icontains')
    flatArea = RangeFilter(field_name="flatArea", lookup_expr='icontains')

