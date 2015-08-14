from django.contrib import admin
from django.utils.safestring import mark_safe
import reversion

# Register your models here.
from .models import (Info,
                     PhoneNumber,
                     LinkList,
                     MOTDMessage)

@admin.register(Info)
class InfoAdmin(reversion.VersionAdmin):
    list_display = ('tag', 'subject', 'created')
    list_display_links = list_display
    search_fields = ('subject', 'details')
    list_filter = ('tag', 'created')

@admin.register(PhoneNumber)
class PhoneNumberAdmin(reversion.VersionAdmin):
    list_display = ('name', 'number')
    list_display_links = list_display
    search_fields = ('name', 'number', 'comment')

@admin.register(LinkList)
class LinkListAdmin(reversion.VersionAdmin):
    list_display = ('name', 'display_on_dashboard', 'display_url')
    list_editable = ('display_on_dashboard',)
    def display_url(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(obj.url, obj.url))

@admin.register(MOTDMessage)
class MOTDAdmin(reversion.VersionAdmin):
    list_display = ('subject',)
