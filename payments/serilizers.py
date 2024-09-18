from rest_framework import serializers
from .models import Customer,Subscription

class SubscriptionSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'

class CustomerSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'