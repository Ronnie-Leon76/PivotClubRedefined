from django.contrib import admin
from rangefilter.filters import DateTimeRangeFilter

from blog.models import Article, Genre, ArticleReview


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    actions = ['approve_comments']
    list_display = ["title", 'author', 'is_reviewed', 'last_modified', 'created_on']
    prepopulated_fields = {'slug': ('title',), }
    # readonly_fields = ('photo', 'title', 'body', 'author', 'claps')
    list_filter = (
        ('created_on', DateTimeRangeFilter), ('last_modified', DateTimeRangeFilter),
    )

    def approve_comments(self, queryset):
        queryset.update(status=True)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Genre)
admin.site.register(ArticleReview)
