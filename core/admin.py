from django.contrib import admin

from core.models import Category, SubCategory, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['category', 'subcategory', 'name', 'price']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


# Register models here.
admin.site.site_header = "Jamal Coffee Shop"
admin.site.site_title = "Jamal Coffee Shop Portal"
admin.site.index_title = "Jamal Coffee Shop Portal"
