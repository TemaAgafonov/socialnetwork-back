from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
   list_display = ('id', 'name', 'followed', 'photo', 'city', 'country')
   list_display_links = ('id',)
   search_fields = ('id', 'name', 'followed',)
   # list_editable = ('name', 'family',)
   list_filter = ('name', 'followed', 'city',)

admin.site.register(User, UserAdmin)
