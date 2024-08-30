from rest_framework import serializers
from .models import Startup, Investor
from .models import Matching

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matching
        fields = '__all__'