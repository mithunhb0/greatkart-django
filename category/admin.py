from django.contrib import admin

from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    # make prepopulated fields
    prepopulated_fields = {'slug': ('category_name',)}
    
    # fields to display
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)
