from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

from blog.models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    actions = ['approve_comments']
    list_display = ["title", 'author', 'is_reviewed', 'last_modified', 'created_on']

    readonly_fields = ('photo', 'title', 'body', 'author', 'claps')
    list_filter = (
        ('created_on', DateTimeRangeFilter), ('last_modified', DateTimeRangeFilter),
    )

    def approve_comments(self, request, queryset):
        queryset.update(status=True)


admin.site.register(Article, ArticleAdmin)
