from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

#from .models import Profile
from .models import ProfileEmp, ProfileFree

# Register your models here.

#admin.site.register(Profile)
admin.site.register(ProfileEmp)
admin.site.register(ProfileFree)


class ProfileInlineE(admin.StackedInline):
    model = ProfileEmp
    can_delete = False
    verbose_name_plural = 'Profile Employee'
    fk_name = 'user'

class ProfileInlineF(admin.StackedInline):
    model = ProfileFree
    can_delete = False
    verbose_name_plural = 'Profile Freelancer'
    fk_name = 'user'

#class ProfileInline(admin.StackedInline):
#    model = Profile
#    can_delete = False
#    verbose_name_plural = 'Profile'
#    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    #inlines = (ProfileInline, )
    inlines = (ProfileInlineE, ProfileInlineF, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_freelancer', 'get_employee', 'is_active', 'is_staff', 'is_superuser')
    #list_select_related = ('profile', )
    list_select_related = ('profileemp', 'profilefree', )

    #def get_superuser(self, instance):
    #    return instance.profile.superuser
    #get_superuser.short_description = 'SuperUser'

    def get_freelancer(self, instance):
    #    return instance.profile.freelancer
        return instance.profilefree.freelancer
    get_freelancer.short_description = 'Freelancer'

    def get_employee(self, instance):
    #    return instance.profile.employee
        return instance.profileemp.employee
    get_employee.short_description = 'Employee'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
