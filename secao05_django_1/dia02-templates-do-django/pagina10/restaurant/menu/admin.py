from django.contrib import admin
from menu.models import Recipe

admin.site.site_header = 'Recipe Manager Admin Panel'
admin.site.register(Recipe)
