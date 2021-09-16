from django.contrib import admin

from .models import GliderReview

class GliderReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'glider', 'user')
    search_fields = ['id', 'glider', 'user']

admin.site.register(GliderReview, GliderReviewAdmin)