from django.contrib import admin
from jobs.models import Job, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'status')


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'type', 'status')
    list_filter = ('category',)
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Job, JobAdmin)
