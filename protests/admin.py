# protests/admin.py
from django.contrib import admin
from .models import Protest, Topic, Role, Participant

admin.site.register(Protest)
admin.site.register(Topic)
admin.site.register(Role)
admin.site.register(Participant)
