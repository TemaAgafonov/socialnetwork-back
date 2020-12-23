from django.contrib import admin
from django.utils.html import format_html

from .models import User, Photo


class PhotoInline(admin.TabularInline):
    model=Photo

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'followed', 'city', 'country', 'small_image_tag', 'large_image_tag')
    inlines = [PhotoInline, ]
    search_fields = ('name', )
    list_editable = ('city', 'country')
    list_filter = ('city',)


    def photos_small(self, x):
        return x.photos.small
    photos_small.short_description = 'small'

    def photos_large(self, x):
        return x.photos.large
    photos_large.short_description = 'large'

    def small_image_tag(self, x):
        return format_html('<img src="{0}" style="width: 100px; height:100px;" />'.format(x.photos.small.url))

    def large_image_tag(self, x):
        return format_html('<img src="{0}" style="width: 150px; height:150px;" />'.format(x.photos.large.url))

    small_image_tag.admin_order_field = 'Маленькая Авка'
    small_image_tag.short_description = 'Small avatar'
    large_image_tag.admin_order_field = 'Большая Авка'
    large_image_tag.short_description = 'Big avatar'

admin.site.register(User, UserAdmin)
