# sitewomen\women\admin.py
from django.contrib import admin, messages
from .models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = "Стутус Жанщин"
    parameter_name = "Stutus"

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замжен'),
            ('single', ' ОДИН ДОМА')
        ]

    def queryset(self, request, queryset):
        if self.value() == "married":
            return queryset.filter(husband__isnull=False)
        elif self.value() == "single":
            return queryset.filter(husband__isnull=True)
        else:
            return queryset


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "is_published", "cat", "brief_info")
    list_display_links = ("id", "time_create")
    ordering = ["time_create"]
    list_editable = ("is_published", "title", "cat")
    # list_per_page = 1
    actions = ["set_published", "set_draft"]
    search_fields = ["title", "cat__name"]
    list_filter = ["is_published", "cat", MarriedFilter]

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
