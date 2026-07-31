# sitewomen\women\admin.py
from django.contrib import admin
from .models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "is_published", "cat")
    list_display_links = ("id", "time_create")
    ordering = ["time_create"]
    list_editable = ("is_published", "title", "cat")
    # list_per_page = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name", "slug")

# Register your models here. 
# admin.site.register(Women, WomenAdmin)
