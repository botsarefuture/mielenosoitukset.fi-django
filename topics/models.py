from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_demonstrations(self):
        return self.protest_set.all()
