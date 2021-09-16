from django.contrib import admin
from .models import CompareItems, SizeItem


class CompareItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'complete')
    search_fields = ['id', 'user']

class SizeItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'size', 'compareItems')
    search_fields = ['id', 'size', 'compareItems']

admin.site.register(CompareItems, CompareItemsAdmin)
admin.site.register(SizeItem, SizeItemsAdmin)