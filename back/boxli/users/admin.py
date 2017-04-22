from django.contrib import admin

from users.models import AdminUser

class UserAdmin(admin.ModelAdmin):
    exclude = ('password',)
    readonly_fields = ('password',)

user_models = (
    AdminUser,
)

admin.site.register(user_models, UserAdmin)

