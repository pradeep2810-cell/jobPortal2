from django.contrib import admin
from django.template.defaultfilters import safe
from information.models import Information, Section


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')


class InformationAdmin(admin.ModelAdmin):
    list_display = ('section', 'title', 'content', 'status')

    def content(self, obj):
        return safe(obj.details)


admin.site.register(Information, InformationAdmin)
admin.site.register(Section, SectionAdmin)
