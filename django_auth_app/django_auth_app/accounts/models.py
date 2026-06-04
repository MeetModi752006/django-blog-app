from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Extends Django's built-in User model with a role field.
    Each User gets exactly one UserProfile (OneToOne relationship).
    """

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('regular', 'Regular User'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='regular')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

    def is_admin_role(self):
        """Helper to check if this user has the admin role."""
        return self.role == 'admin'
