from django.contrib import admin
from .models import Maker,Glider,Size

class MakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'account')
    search_fields = ['id', 'name', 'account']

class GliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'maker', 'year')
    search_fields = ['id', 'name', 'maker', 'year']

class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'glider', 'size')
    search_fields = ['id', 'glider', 'size']

admin.site.register(Maker, MakerAdmin)
admin.site.register(Glider, GliderAdmin)
admin.site.register(Size, SizeAdmin)
