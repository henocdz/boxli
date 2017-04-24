from django.contrib import admin

from users.models import *

class UserAdmin(admin.ModelAdmin):
    exclude = ('password',)
    readonly_fields = ('password',)

user_models = (
    User, UserToken
)

admin.site.register(AdminUser, UserAdmin)
admin.site.register(user_models)

