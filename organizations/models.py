from django.db import models
from django.urls import reverse


class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    date_of_foundation = models.DateField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    activism_focus = models.TextField(blank=True, null=True)
    
    logo = models.ImageField(upload_to='organization_logos/', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('organization_detail', kwargs={'organization_id': self.pk})
    
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
