from rest_framework import serializers
from .models import (
    Startup, 
    StartupDetails, 
    StartupOffering, 
    StartupFinancials, 
    StartupImpact, 
    StartupTeam, 
    StartupMarket, 
    StartupMatchingPreferences
)

from .models import Investor

class StartupDetailsSerializer(serializers.ModelSerializer):
    startup = serializers.PrimaryKeyRelatedField(read_only=True)  # Set to read-only

    class Meta:
        model = StartupDetails
        fields = '__all__'

class StartupOfferingSerializer(serializers.ModelSerializer):
    startup = serializers.PrimaryKeyRelatedField(read_only=True)  # Set to read-only

    class Meta:
        model = StartupOffering
        fields = '__all__'

class StartupFinancialsSerializer(serializers.ModelSerializer):
    startup = serializers.PrimaryKeyRelatedField(read_only=True)  # Set to read-only

    class Meta:
        model = StartupFinancials
        fields = '__all__'

class StartupImpactSerializer(serializers.ModelSerializer):
    startup = serializers.PrimaryKeyRelatedField(read_only=True)  # Set to read-only

    class Meta:
        model = StartupImpact
        fields = '__all__'

class StartupTeamSerializer(serializers.ModelSerializer):
    startup = serializers.PrimaryKeyRelatedField(read_only=True)  # Set to read-only

    class Meta:
        model = StartupTeam
        fields = '__all__'

class StartupMarketSerializer(serializers.ModelSerializer):
    startup = serializers.PrimaryKeyRelatedField(read_only=True)  # Set to read-only

    class Meta:
        model = StartupMarket
        fields = '__all__'

class StartupMatchingPreferencesSerializer(serializers.ModelSerializer):
    startup = serializers.PrimaryKeyRelatedField(read_only=True)  # Set to read-only

    class Meta:
        model = StartupMatchingPreferences
        fields = '__all__'

class StartupSerializer(serializers.ModelSerializer):
    details = StartupDetailsSerializer()
    offerings = StartupOfferingSerializer()
    financials = StartupFinancialsSerializer()
    impact = StartupImpactSerializer()
    team = StartupTeamSerializer()
    market = StartupMarketSerializer()
    preferences = StartupMatchingPreferencesSerializer()

    class Meta:
        model = Startup
        fields = '__all__'

    def create(self, validated_data):
        # Extract and remove nested data
        details_data = validated_data.pop('details', None)
        offerings_data = validated_data.pop('offerings', None)
        financials_data = validated_data.pop('financials', None)
        impact_data = validated_data.pop('impact', None)
        team_data = validated_data.pop('team', None)
        market_data = validated_data.pop('market', None)
        preferences_data = validated_data.pop('preferences', None)

        # Create the Startup instance
        startup = Startup.objects.create(**validated_data)

        # Create and associate related objects if data is provided
        if details_data:
            details = StartupDetails.objects.create(startup=startup, **details_data)
            startup.details = details

        if offerings_data:
            offerings = StartupOffering.objects.create(startup=startup, **offerings_data)
            startup.offerings = offerings

        if financials_data:
            financials = StartupFinancials.objects.create(startup=startup, **financials_data)
            startup.financials = financials

        if impact_data:
            impact = StartupImpact.objects.create(startup=startup, **impact_data)
            startup.impact = impact

        if team_data:
            team = StartupTeam.objects.create(startup=startup, **team_data)
            startup.team = team

        if market_data:
            market = StartupMarket.objects.create(startup=startup, **market_data)
            startup.market = market

        if preferences_data:
            preferences = StartupMatchingPreferences.objects.create(startup=startup, **preferences_data)
            startup.preferences = preferences

        # Save the updated Startup instance
        startup.save()

        return startup
    
    def update(self, instance, validated_data):
        # Update each related field manually
        if 'details' in validated_data:
            details_data = validated_data.pop('details')
            for attr, value in details_data.items():
                setattr(instance.details, attr, value)
            instance.details.save()

        if 'offerings' in validated_data:
            offerings_data = validated_data.pop('offerings')
            for attr, value in offerings_data.items():
                setattr(instance.offerings, attr, value)
            instance.offerings.save()

        if 'financials' in validated_data:
            financials_data = validated_data.pop('financials')
            for attr, value in financials_data.items():
                setattr(instance.financials, attr, value)
            instance.financials.save()

        if 'impact' in validated_data:
            impact_data = validated_data.pop('impact')
            for attr, value in impact_data.items():
                setattr(instance.impact, attr, value)
            instance.impact.save()

        if 'team' in validated_data:
            team_data = validated_data.pop('team')
            for attr, value in team_data.items():
                setattr(instance.team, attr, value)
            instance.team.save()

        if 'market' in validated_data:
            market_data = validated_data.pop('market')
            for attr, value in market_data.items():
                setattr(instance.market, attr, value)
            instance.market.save()

        if 'preferences' in validated_data:
            preferences_data = validated_data.pop('preferences')
            for attr, value in preferences_data.items():
                setattr(instance.preferences, attr, value)
            instance.preferences.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
        
from .models import Investor, InvestorPreferences, InvestorPortfolio

class InvestorPreferencesSerializer(serializers.ModelSerializer):
    investor = serializers.PrimaryKeyRelatedField(read_only=True)  # Set to read-only

    class Meta:
        model = InvestorPreferences
        fields = '__all__'

class InvestorPortfolioSerializer(serializers.ModelSerializer):
    investor = serializers.PrimaryKeyRelatedField(read_only=True)  # Set to read-only

    class Meta:
        model = InvestorPortfolio
        fields = '__all__'

class InvestorSerializer(serializers.ModelSerializer):
    preferences = InvestorPreferencesSerializer()
    portfolio = InvestorPortfolioSerializer()

    class Meta:
        model = Investor
        fields = '__all__'

    def create(self, validated_data):
        preferences_data = validated_data.pop('preferences', None)
        portfolio_data = validated_data.pop('portfolio', None)

        investor = Investor.objects.create(**validated_data)

        if preferences_data:
            preferences = InvestorPreferences.objects.create(investor=investor, **preferences_data)
            investor.preferences = preferences

        if portfolio_data:
            portfolio = InvestorPortfolio.objects.create(investor=investor, **portfolio_data)
            investor.portfolio = portfolio

        investor.save()
        return investor

    def update(self, instance, validated_data):
        if 'preferences' in validated_data:
            preferences_data = validated_data.pop('preferences')
            for attr, value in preferences_data.items():
                setattr(instance.preferences, attr, value)
            instance.preferences.save()

        if 'portfolio' in validated_data:
            portfolio_data = validated_data.pop('portfolio')
            for attr, value in portfolio_data.items():
                setattr(instance.portfolio, attr, value)
            instance.portfolio.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance