from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Startup
from .models import Investor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",'username', 'first_name', 'last_name', 'email', "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = ("id", "name", "stage", "industry", "capital", "impact", "sdg", "values", "expertise",'location' "matching", "strategy", "created_at", "startup_owner")

        extra_kwargs = {"owner": {"read_only": True}}

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor 
        fields = ('id', 'name', 'stage', 'industry','capital', 'impact', 'sdg', 'values', 'expertise', 'location','created_at','investor_owner' )
        extra_kwargs = {"name": {"read_only": True}}

        #TODO: adding extra kwargs for security kubernetes software orchestrazione container insieme a docker google cloud platform aws o asure, collegamento linkedin google social-auth-app-django