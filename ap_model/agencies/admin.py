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


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'parent']
    list_filter = ('type',)
    search_fields = ['user__username']


@admin.register(AshAdmin)
class AshAdminAdmin(admin.ModelAdmin):
    list_display = ['user', 'ash_code', 'ash_username']
    list_filter = ('ash_code',)
    search_fields = ['ash_code', 'ash_name']


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['agent_profile', 'type', 'number']
    list_filter = ('agent_profile__code',)
    search_fields = ['agent_profile', 'agent_profile__code']


@admin.register(Manpower)
class ManpowerAdmin(admin.ModelAdmin):
    list_display = ['agent', 'position']
    #list_filter = ('agent__code',)
    search_fields = ['agent__code']


@admin.register(ManpowerSummary)
class ManpowerSummaryAdmin(admin.ModelAdmin):
    list_display = ['agent_code','tipe']
    list_filter = ('tipe',)
    search_fields = ['agent_code']


@admin.register(ManpowerSummaryNew)
class ManpowerSummaryNewAdmin(admin.ModelAdmin):
    list_display = ['agent_code', 'tipe']
    list_filter = ('tipe',)
    search_fields = ['agent_code']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_filter = ('agent_profile',)
    search_fields = ['agent_profile__code', 'agent_profile__code']


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['agent_profile', 'name', 'account_holder_name']
    list_filter = ('name',)
    search_fields = ['name', 'account_no', 'account_holder_name']


@admin.register(DepartmentCategory)
class DepartmentCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ('name',)
    search_fields = ['name']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'department_category', 'name']
    list_filter = ('department_category',)
    search_fields = ['name']


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ['department_category', 'department', 'type', 'target', 'name', 'filename']
    #list_display = ['type', 'target', 'name', 'filename']
    list_filter = ('type', 'target', 'department')
    #list_filter = ('type', 'target')
    search_fields = ['name', 'department']
    #search_fields = ['name']


@admin.register(AgentNewRecruit)
class AgentNewRecruitAdmin(admin.ModelAdmin):
    list_display = ['leader_agent', 'recruited_code', 'recruiter_code']
    list_filter = ['leader_agent__code', 'recruiter_code__code']
    search_fields = ['leader_agent__code', 'recruiter_code__code']


@admin.register(AgentDashboard)
class AgentDashboardAdmin(admin.ModelAdmin):
    list_display = ['agent', 'group']
    list_filter = ['group']
    search_fields = ['agent__code']


@admin.register(AccountLockoutNew)
class AccountLockoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'lock_count', 'is_locked', 'lock_until']
    search_fields = ['user__username']


@admin.register(TakumiDashboard)
class TakumiDashboardAdmin(admin.ModelAdmin):
    list_display = ['agent', 'group']
    list_filter = ['group']
    search_fields = ['agent__code']


@admin.register(AgentLevelAsh)
class AgentLevelAshAdmin(admin.ModelAdmin):
    list_display = ['agent_code', 'position', 'amb_code', 'rmb_code', 'rd_code', 'ash_code']
    list_filter = ['ash_code', 'rd_code', 'position']
    search_fields = ['agent_code']


@admin.register(Notifications)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'target', 'priority', 'title', 'start', 'end']
    list_filter = ['target',]
    search_fields = ['user__username']


@admin.register(DashBoardImageSlider)
class DashBoardImageSliderAdmin(admin.ModelAdmin):
    exclude = ['author']
    search_fields = ['published']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(DashBoardImageSliderAdmin, self).save_model(request, obj, form, change)


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['user', 'department', 'rd_code']
    list_filter = ['user__username',]
    search_fields = ['user__username']


@admin.register(UserDepartment)
class UserDepartmentAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'description']
    list_filter = ['name']
    search_fields = ['name']

