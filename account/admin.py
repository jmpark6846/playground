from django.contrib import admin
from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'email',
        'username',
        'is_staff',
        'creation_date'
    )

    list_display_links = (
        'email',
        'username',
    )
