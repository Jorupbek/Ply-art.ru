from django.contrib import admin
from django.utils.html import format_html

from pages.models import Slider, Contacts, Faq, Pages, About, Colors

site_header = 'Ply-Art Админ панель'


class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_display_links = ('title', 'is_active', 'created_at')


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'address')
    list_display_links = ('phone_number', 'email', 'address')


class PagesListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Slider, SliderAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Faq)
admin.site.register(About)
admin.site.register(Colors)
admin.site.register(Pages, PagesListAdmin)

# register admin name
admin.site.site_header = format_html(site_header)
