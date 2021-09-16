from django.forms import ModelForm, IntegerField, NumberInput

from .models import GliderReview

class ReviewCreation(ModelForm):
    class Meta:
        model = GliderReview
        fields = ['content','stars']
        widgets = {
            'stars': NumberInput(attrs={'min': '0','max': '5'}),
        }

