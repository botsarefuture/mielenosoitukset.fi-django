from django.db import models
from organizations.models import Organization
from topics.models import Topic
from django.contrib.auth.models import User

from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    incompatible_roles = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.name


from django.core.exceptions import ValidationError
from django.db import models
from organizations.models import Organization
from topics.models import Topic

from django.db import models
from django.conf import settings
from organizations.models import Organization
from topics.models import Topic

class Protest(models.Model):
    title = models.CharField(max_length=255, null=True)

    location = models.CharField(max_length=100)
    date = models.DateField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic)
    details = models.TextField()  # Add details for the protest/demonstration
    image = models.ImageField(upload_to='demonstration_images/', null=True)  # Adjust the upload path as needed

    # Add more fields as needed

    def __str__(self):
        return f"{self.location} - {self.date}"


class Participant(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    protest = models.ForeignKey(Protest, on_delete=models.CASCADE)
    # Add more fields as needed

    def clean(self):
        # Custom validation logic
        incompatible_roles = self.role.incompatible_roles.all()

        for incompatible_role in incompatible_roles:
            if self.participant_set.filter(role=incompatible_role).exists():
                raise ValidationError(f"The selected role '{self.role}' is incompatible with existing roles.")

    def __str__(self):
        return f"{self.name} - {self.protest}"
