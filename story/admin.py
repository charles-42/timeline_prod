from django.contrib import admin

# Register your models here.

from .models import Events

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    search_fields = ['date', 'name']
    list_display = ('date', 'category','name','autor')
