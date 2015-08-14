from django.contrib import admin
import reversion

# Register your models here.
from .models import Info 
from .models import PhoneNumber 

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
