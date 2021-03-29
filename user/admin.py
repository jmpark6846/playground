from django.contrib import admin
from .models import User, UserProfile, WorkExperience


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'username',
        'is_staff',
        'created_at'
    )

    list_display_links = (
        'email',
        'username',
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)

admin.site.register(WorkExperience)
