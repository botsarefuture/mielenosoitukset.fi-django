# models.py
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from modeltranslation.translator import TranslationOptions, register
from organizations.models import Organization
from topics.models import Topic
from django.urls import reverse


class UpcomingProtestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(date__gte=timezone.now())

class Protest(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=100)
    date = models.DateTimeField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic)
    details = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='demonstration_images/', blank=True, null=True)

    objects = models.Manager()
    upcoming_protests = UpcomingProtestManager()
    
    def get_absolute_url(self):
        return reverse('protest_detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.location} - {self.date}"



class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    incompatible_roles = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.name


class Participant(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    protest = models.ForeignKey(Protest, on_delete=models.CASCADE)

    def clean(self):
        incompatible_roles = self.role.incompatible_roles.all()

        for incompatible_role in incompatible_roles:
            if self.participant_set.filter(role=incompatible_role).exists():
                raise ValidationError(f"The selected role '{self.role}' is incompatible with existing roles.")

    def __str__(self):
        return f"{self.name} - {self.protest}"
