from django.contrib import admin
from .models import *

class PatternBaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'slug', 'visible', 'order',)
    list_editable = ('visible', 'order',)

class PatternInline(admin.StackedInline):
    model = Pattern

class PatternCategoryAdmin(PatternBaseAdmin):
    list_display = ('title', 'slug', 'visible', 'order',)
    inlines = [ PatternInline ]

admin.site.register(PatternCategory, PatternCategoryAdmin)
admin.site.register(Pattern, PatternBaseAdmin)
