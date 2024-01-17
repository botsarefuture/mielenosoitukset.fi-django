from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from organizations.models import Organization

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    USER_ROLES = [
        ('member', 'Member'),
        ('admin', 'Admin'),
        ('owner', 'Owner'),
    ]

    role = models.CharField(max_length=20, choices=USER_ROLES, default='member')
    organization = models.OneToOneField(Organization, on_delete=models.SET_NULL, null=True, blank=True)

    # Provide a unique related_name for the groups field
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='customuser_groups_set',
        related_query_name='user',
    )

    # Provide a unique related_name for the user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_permissions_set',
        related_query_name='user',
    )

    def __str__(self):
        return self.email
    
    
