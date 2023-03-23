from django.contrib import admin

from .models import Menu

# admin.site.register(Menu)


class MenuInline(admin.TabularInline):
    model = Menu
    fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title', )}
    extra = 3


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')
    prepopulated_fields = {'slug': ('title', )}
    inlines = (MenuInline, )
