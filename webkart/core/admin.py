'''django admin customisation'''

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    '''define the admin pages for users'''
    ordering = ['id']
    list_display = ['email', 'name', 'is_seller']

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password',
                )
            }
        ),
        (
            'Details', {
                'fields': (
                'name',
                'number',
                'is_seller',
            )
            }
        ),
        (
            'Permissions', {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (
            'Important Dates and Images', {
                'fields': (
                    'last_login',

                )
            }
        )
    )
    readonly_fields = ['last_login']

    add_fieldsets = (
        (
            None,
            {
                # custom css classes
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'number',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'is_seller',
                )
            }
        ),
    )


admin.site.register(models.User, UserAdmin)
