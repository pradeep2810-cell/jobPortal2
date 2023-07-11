from django.contrib import admin
from applications.models import Application


class AppAdmin(admin.ModelAdmin):
    list_display = ('jobseeker', 'job', 'date', 'status')


admin.site.register(Application, AppAdmin)
