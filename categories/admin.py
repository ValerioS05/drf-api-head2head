from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    category_display = ('name', 'description', 'image')
    category_search = ('name',)
    category_filter = ('name',)
