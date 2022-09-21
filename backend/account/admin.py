from django.contrib import admin

from . models import CustomizeUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id','username']

admin.site.register(CustomizeUser, CustomUserAdmin)