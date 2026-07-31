# sitewomen\women\admin.py
from django.contrib import admin, messages
from .models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "is_published", "cat", "brief_info")
    list_display_links = ("id", "time_create")
    ordering = ["time_create"]
    list_editable = ("is_published", "title", "cat")
    # list_per_page = 1
    actions = ["set_published", "set_draft"]

    @admin.display(description="Ещё Инфа", ordering="content")
    def brief_info(self, women: Women):
        return f"Длинна контента {len(women.content)} и {women.content[:5]}"

    @admin.action(description="Сделать опубликованными")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Измена {count} зуписей на опубликовано")

    @admin.action(description="Убрать опубликованность")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"Измена {count} зуписей и убрана опубликованность", messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name", "slug")

# Register your models here. 
# admin.site.register(Women, WomenAdmin)
