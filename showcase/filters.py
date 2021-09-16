import django_filters
from django.forms import ModelForm, CheckboxSelectMultiple, TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from .models import Glider, Maker, CERTIFICATION_CHOICES
from django_filters import CharFilter,  NumberFilter,RangeFilter, MultipleChoiceFilter



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


    year = NumberFilter(field_name="year")

    class Meta:
        form = GliderFilterForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['maker'].queryset = Maker.objects.all()





class SizeFilter(django_filters.FilterSet):
    certification = MultipleChoiceFilter(field_name= "certification", choices=CERTIFICATION_CHOICES, widget=CheckboxSelectMultiple)
    cells = RangeFilter(field_name="cells")
    gliderWeight = RangeFilter(field_name="gliderWeight")
    projectArea = RangeFilter(field_name="projectArea")
    flatArea = RangeFilter(field_name="flatArea")
    takeoffWeightMin = RangeFilter(field_name="takeoffWeightMin", label="Pilot Min weight")
    takeoffWeightMax = RangeFilter(field_name="takeoffWeightMax", label="Pilot Max weight")

