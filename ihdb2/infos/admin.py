from django.contrib import admin
from django.utils.safestring import mark_safe
import reversion

# Register your models here.
from .models import Info 
from .models import PhoneNumber 
from .models import LinkList 

@admin.register(Info)
class InfoAdmin(reversion.VersionAdmin):
    list_display = ('priority', 'subject', 'created')
    list_display_links = list_display
    search_fields = ('subject', 'details')
    list_filter = ('priority', 'created')

@admin.register(PhoneNumber)
class PhoneNumberAdmin(reversion.VersionAdmin):
    list_display = ('name', 'number')
    list_display_links = list_display
    search_fields = ('name', 'number', 'comment')

@admin.register(LinkList)
class LinkListAdmin(reversion.VersionAdmin):
    list_display = ('name', 'display_url')
    def display_url(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(obj.url, obj.url))
