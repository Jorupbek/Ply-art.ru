from django.contrib import admin

from shop.models import Category, Product, Images, Attributes


class ImagesDetailsInline(admin.StackedInline):
    model = Images


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'in_home']
    list_filter = ['created', 'updated']
    list_editable = ['price', 'in_home']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImagesDetailsInline]


@admin.register(Attributes)
class AttributesAdmin(admin.ModelAdmin):
    list_display = ['name', 'detail']
