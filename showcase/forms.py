from django.forms import ModelForm
from .models import Maker, Glider, Size


class MakerEditForm(ModelForm):
    class Meta:
        model = Maker
        exclude = ['name','account']

class GliderForm(ModelForm):
    class Meta:
        model = Glider
        fields = ['name', 'gliderImage','year']

class SizeForm(ModelForm):
    class Meta:
        model = Size
        exclude = ['glider']