from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')  
admin.site.register(Category, CategoryAdmin)

class PropertiesImagesInline(admin.TabularInline):
    model = PropertyImages  
    extra = 1 
    fields = ('image',) 

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'address', 'old_price', 'new_price', 'is_highlight', 'is_featured', 'status','slug')
    list_filter = ('status', 'is_highlight', 'is_featured')
    search_fields = ('title', 'address', 'description')
    inlines = [PropertiesImagesInline]  
admin.site.register(Property, PropertyAdmin)