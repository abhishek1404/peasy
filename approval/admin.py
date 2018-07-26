# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile, Prescription, RequestQ

class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'id')
admin.site.register(UserProfile, UserAdmin)
admin.site.register(Prescription)
admin.site.register(RequestQ)

# Register your models here.
