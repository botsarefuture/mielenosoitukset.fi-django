# models.py
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Make description optional
    location = models.CharField(max_length=100, blank=True, null=True)  # Make location optional
    date_of_foundation = models.DateField(blank=True, null=True)  # Make date of foundation optional
    contact_email = models.EmailField(blank=True, null=True)  # Make contact email optional
    website = models.URLField(blank=True, null=True)  # Make website optional
    activism_focus = models.TextField(blank=True, null=True)  # Make activism focus optional
    
    logo = models.ImageField(upload_to='organization_logos/', blank=True, null=True)  # Add logo field

    def __str__(self):
        return self.name


class Membership(models.Model):
    ACCESS_LEVEL_CHOICES = [
        ('member', 'Member'),
        ('admin', 'Admin'),
        ('owner', 'Owner'),
    ]

    user = models.ForeignKey(
        'users.CustomUser',
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
