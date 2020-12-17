from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'followed', 'photo', 'city', 'country')
    list_display_links = ('id',)
    search_fields = ('id', 'name', 'followed',)
    list_filter = ('name', 'followed', 'city',)

admin.site.register(User, UserAdmin)
