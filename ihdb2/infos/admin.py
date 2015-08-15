from django.contrib import admin
from django.utils.safestring import mark_safe
import reversion

# Register your models here.
from .models import (Info,
                     PhoneNumber,
                     LinkList,
                     MOTDMessage,
                     Beamer)


@admin.register(Info)
class InfoAdmin(reversion.VersionAdmin):
    list_display = ('tag', 'subject', 'modified', 'created', 'created_by', 'modified_by')
    list_display_links = list_display
    search_fields = ('subject', 'details')
    list_filter = ('tag', 'created')


@admin.register(PhoneNumber)
class PhoneNumberAdmin(reversion.VersionAdmin):
    list_display = ('name', 'number', 'created_by', 'modified_by')
    list_display_links = list_display
    search_fields = ('name', 'number', 'comment')


@admin.register(LinkList)
class LinkListAdmin(reversion.VersionAdmin):
    list_display = ('name', 'display_on_dashboard', 'display_url', 'created_by', 'modified_by')
    list_editable = ('display_on_dashboard',)

    def display_url(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(obj.url, obj.url))


@admin.register(MOTDMessage)
class MOTDAdmin(reversion.VersionAdmin):
    list_display = ('subject', 'created_by', 'modified_by')


@admin.register(Beamer)
class BeamerAdmin(reversion.VersionAdmin):
    list_display = ('beamer', 'returned', 'lent_to', 'created', 'created_by', 'modified_by')
    list_display_links = list_display
    list_filter = ('returned', 'beamer')
    search_fields = ('lent_to',)
