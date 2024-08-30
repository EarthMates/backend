from django.db import models
from django.conf import settings
from api.models import Investor
from users.models import CustomUser
from api.models import Startup


# Create your models here.
class Matching(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name= 'user')
    matched_with = models.CharField(max_length=255)
    match_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_delivered = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "matched_with")
