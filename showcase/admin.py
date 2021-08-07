from django.contrib import admin
from showcase.models import Maker,Glider,Size, GliderReview

# Register your models here.
admin.site.register(Maker)
admin.site.register(Glider)
admin.site.register(Size)
admin.site.register(GliderReview)