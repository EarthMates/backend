from django.db import models
from django.contrib.auth.models import User
import string
import random

# Create your models here.

class Startup(models.Model):
    name = models.CharField(max_length=255)
    stage = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    capital = models.DecimalField(max_digits=15,decimal_places=0)
    impact = models.DecimalField(max_digits=10, decimal_places=0)
    sdg = models.JSONField()
    values = models.JSONField()
    expertise = models.JSONField()
    matching = models.JSONField()
    strategy = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name="startups", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Routines to check boundries of data:
# - name none
# - stage in ["Pre Seed", "Series A", "Series B", "Series C", "Bridge"]
# - industry in ["Finance", "Agricolture", "Technology", "Mobility"]
# - location in ["Rwanda", "Ghana", "Nigeria"]
# - 10000 <= capital required <= 100 M


# Investor model:
# - name
# - stage
# - industry
# - location

# Routines to check boundries of data:
# - name none
# - stage in ["Pre Seed", "Series A", "Series B", "Series C", "Bridge"]
# - industry in ["Finance", "Agricolture", "Technology", "Mobility"]
# - location in ["Rwanda", "Ghana", "Nigeria"]