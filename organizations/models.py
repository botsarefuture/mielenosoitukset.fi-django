# models.py
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # Add the founding_date field
    founding_date = models.DateField(null=True)

    def __str__(self):
        return self.name


from django.db import models
from users.models import CustomUser

from django.db import models
from users.models import CustomUser
class Membership(models.Model):
    ACCESS_LEVEL_CHOICES = [
        ('member', 'Member'),
        ('admin', 'Admin'),
        ('owner', 'Owner'),
    ]

    user = models.ForeignKey(
        'users.CustomUser',  # Use string reference to break circular dependency
        on_delete=models.CASCADE,
    )

    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        related_name='memberships',
    )

    access_level = models.CharField(max_length=20, choices=ACCESS_LEVEL_CHOICES, default='member')

    def __str__(self):
        return f"{self.user.username} - {self.organization.name}"