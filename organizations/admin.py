from django.contrib import admin
from django.template.defaultfilters import safe
from django.utils.html import format_html

from organizations.models import Organization, OrgUser


class OrgAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'phone', 'email', 'type', 'status')
    radio_fields = {'type': admin.VERTICAL}

    def get_image(self, obj):
        return format_html(f'<img src="/media/{obj.logo}" style="height:100px; width:100px;" />')


admin.site.register(Organization, OrgAdmin)
admin.site.register(OrgUser)
