from django.forms import ModelForm

from .models import GliderReview

class ReviewCreation(ModelForm):
    class Meta:
        model = GliderReview
        fields = ['content','stars']