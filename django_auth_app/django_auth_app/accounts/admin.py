from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'created_at']
    list_filter = ['role']
    search_fields = ['user__username', 'user__email']

    # Allow admins to change user roles from the admin panel
    fields = ['user', 'role', 'bio', 'avatar']
