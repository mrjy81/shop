from django.contrib import admin

from django.contrib.sessions.models import Session
import json


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        try:
            product = obj.get_decoded()['products']
        except KeyError:
            return obj.get_decoded()
        else:
            return product

    list_display = ['session_key', '_session_data', 'expire_date']


admin.site.register(Session, SessionAdmin)
