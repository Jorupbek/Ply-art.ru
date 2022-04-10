from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from shop.models import Category, Product, Images, Attributes


class ImagesDetailsInline(admin.StackedInline):
    model = Images


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug', 'position', 'in_home']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('position',)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug', 'price', 'in_home']
    list_filter = ['created', 'updated']
    list_editable = ['price', 'in_home']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImagesDetailsInline]


@admin.register(Attributes)
class AttributesAdmin(ImportExportModelAdmin):
    list_display = ['name', 'detail']
