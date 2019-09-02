from django.contrib import admin
from ap_model.agencies.models import *


# Register your models here.
@admin.register(AgentProfile)
class AgentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'branch', 'code']
    list_filter = ('status', 'branch__name',)
    search_fields = ['code', 'user__username']


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'office_code']
    list_filter = ('name',)
    search_fields = ['name', 'address']


@admin.register(UserBranch)
class UserBranchAdmin(admin.ModelAdmin):
    list_display = ['user', 'branch']
    list_filter = ('branch__name',)
    search_fields = ['user__username', 'branch__name']