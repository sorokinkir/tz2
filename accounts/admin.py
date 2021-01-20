from django.contrib import admin
from . import models


@admin.register(models.Users)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')
    list_filter = ('user',)
