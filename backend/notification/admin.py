from django.contrib import admin
from . models import Notification

# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'game','sender','receiver','notification_types']
    search_fields = ['sender', 'receiver', 'game']

admin.site.register(Notification, NotificationAdmin)