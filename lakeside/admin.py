from django.contrib import admin
from lakeside.models import Category, Style, Inner

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat_name', 'cat_image']
    list_editable = ['cat_name', 'cat_image']
    
@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_id', 'category', 'name', 'image', 'special', 'breakfast', 'lunch', 'dinner', 'appetizer', 'dessert', 'drink', 'price', 'min', 'max', 'in_stock' ]
    list_editable = ['special']
    
@admin.register(Inner)
class InnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'inner_name', 'inner_rep', 'inner_image']
    list_editable = ['inner_name', 'inner_image', 'inner_rep']